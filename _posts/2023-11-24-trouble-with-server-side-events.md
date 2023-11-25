---
title: "The Trouble With Server Side Events"
date: 2023-11-24
published: true
visible: true
categories:
  - Blog
tags:
  - spring-boot
  - server-side-events
toc: false
classes: wide
---
# SSE Connection Lost Detection Delay Issue and Solutions

Server Side Events  for Server to Browser communication can be used to inform the clients about server side updates to the data the client browser shows to the user. Then e.g. a  Frontend Single Page application can decide to reload new data from the server.

When implementing this solution with Spring boot and Angular for a project, we observed that if the SSE - Connection timeout is set to infinity on the server side, even if the server sends keepalive events to the client every 10 - 30 seconds to avoid broken connections, the server detects broken connection only after about 10 min or so. This comes from  `RTO` of up to 60sec and `tcp_retries2` of 15, as explained below.
Moreover, we observed, that server sends keepalive events to the client every 10sec seems necessary in some environments to prevent the network infrastructure (firewalls etc.) from dropping the connection prematurely.

In this blog post, we explore the reasons behind this observation and potential solutions like WebSockets and limiting SSE connection duration on the server side, while also addressing why such a delay of 10 min for detecting broken connections is problematic:

- **Problem of Delayed Detection**: A 10-minute delay in detecting broken connections is problematic because it can lead to **inefficient resource use**, as the server continues to allocate resources to a connection that is effectively dead. This inefficiency can impact server performance and limit its capacity to handle active users.

## TCP and SSE Limitations
The delay in detecting broken connections with SSE is significantly influenced by the underlying TCP protocol's characteristics and the nature of SSE itself:

- **Unidirectional Communication of SSE**: SSE is inherently unidirectional, only allowing data flow from the server to the client. This design lacks a mechanism for the client to send periodic acknowledgments or keep-alive signals back to the server, making it challenging for the server to promptly detect if the client has disconnected or if the connection has been interrupted.

- **Reliance on TCP's Timeout Mechanisms**: SSE operates over TCP, which employs timeout mechanisms to detect lost packets and connection issues. These mechanisms include the calculation of `Retransmission Timeouts` (`RTO`) and the use of exponential backoff strategies for packet retransmissions. However, TCP is designed to be conservative in declaring a connection as broken to handle transient network issues gracefully. This often results in default TCP timeouts being set to several minutes, leading to delays in the detection of connection losses in SSE.

- **Initial and Subsequent RTOs**: TCP's initial RTO is typically around 1 second but adapts based on ongoing Round-Trip Time (RTT) measurements up to **60 sec** . The RTO increases exponentially upon consecutive retransmission timeouts (exponential backoff), which can lead to substantial delays in recognizing a connection as broken, especially under fluctuating network conditions.

- **System-Level TCP Settings**: Linux TCP settings `tcp_retries1` and `tcp_retries2` contribute to the time taken to detect broken connections. `tcp_retries2` is **15** on a typical linux OS

- **Lack of Immediate Feedback in TCP**: TCP does not provide immediate feedback to the application layer about the state of the connection. The protocol needs to go through multiple timeout cycles and retransmissions before it concludes that the connection is no longer active. This process is time-consuming, and during this period, the application layer (SSE in this case) remains unaware of the broken connection.

- **Impact on SSE Performance**: Due to these TCP characteristics, an SSE server might continue attempting to send events to a client that is no longer connected, leading to wasted server resources and potential issues in application performance, especially in scenarios requiring real-time data exchange or high user concurrency.

The combination of SSE's unidirectional communication model and TCP's conservative approach to connection management leads to inherent delays in detecting disconnections in SSE-based applications.

## Solutions

3. **WebSocket Solution**: Using WebSockets can solve this issue by enabling bidirectional communication, allowing for real-time detection of connection issues and more efficient resource management.

4. **Limiting SSE Connection Duration**: Configuring SSE connections to be short-lived (e.g., 30 seconds) forces clients to reconnect periodically, enabling quicker detection of broken connections at the cost of increased overhead. 

9. **Client-To-Server Keepalives**: To achieve more responsive connection management, custom solutions such as bidirectional keep-alives or enhanced monitoring are required but are not inherently supported in SSE or Spring Boot.

**Remark:** When using Spring Boot 3.x the default value for the timeout for SSE is 30sec anyhow. It can also be set to infinity, which only works as long as keepalive events are send by the server every 10 sec or so.

In conclusion, the considerable delay in detecting broken SSE connections presents a challenge in terms of resource efficiency and server performance. While SSE has benefits, its dependency on TCP and lack of bidirectional communication can lead to significant delays in recognizing disconnected clients. Adopting alternatives like **WebSockets** or **implementing strategies to limit connection duration** can offer more immediate detection and better resource management, though they come with their own trade-offs and implementation requirements.

