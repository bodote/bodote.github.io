## Praxis

Java Stream (`System.in`, `System.out`)Grundlagen klar ?

Analogie : Stellmotor für einen Raketenmotor: Fazit : Testbed / Fixture zu bauen kann aufwendig sein, ist es aber Wert zu tun.

### Hello World TDD style mit java / gradle / junit5

- Lösung:  
  `mkdir newDir; cd newDir; gradle init --type java-application`
- ignoriere `App.java` und `AppTest.java` erstmal
- lege erst Testclasse MyAppTest an
- füge Test für MyAppTest.main(String\[\] args) hinzu
- wie schreibe ich auf commandline mit Java ? `System.out.println("bla")`
- wie teste ich `System.out.println("bla")` ?  
  \`\`\`java  
  import org.junit.jupiter.api.AfterEach;  
  import org.junit.jupiter.api.BeforeEach;  
  import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;  
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.\*;

class MyTest {

```
private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
private final PrintStream originalOut = System.out;

@BeforeEach
public void setUpStreams() {
    System.setOut(new PrintStream(outContent));
}

@AfterEach
public void restoreStreams() {
    System.setOut(originalOut);
}

@Test
void testPrint() {
    System.out.println("bla");

    assertEquals("bla\n", outContent.toString());
}
```

}
