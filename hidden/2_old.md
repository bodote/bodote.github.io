# Calculator
### Anforderungen :
- ändere dein `Hello world!` so , dass statt "Hello world!" der String "Caclulator, addition, gebe ersten Summanden ein:" angezeigt wird
- ergänze, dass ein String eingegeben werden kann, sobald der mit "Enter"  vom Benutzer abgeschlossen wird erscheint eine weitere Meldung "und bitte jetzt 2. Summand:"
- ergänze dass auch dieser  String eingegeben werden kann, bis die Eingabe mit "Enter"  vom Benutzer abgeschlossen wird 
- gebe aus "Summe:" und dann die Summe der beiden Zahlen.
- berücksichtige zunächst nur Ganzzahlen aber keine Kommazahlen oder gar ungültige Strings, die keine Zahlen sind.

## Hinweise für den Test:
So ähnlich wie man `System.out` zu Testzwecken umleiten kann,  kann man das auch mit `System.in` machen. 

```java
//...
private final InputStream originalSystemIn = System.in;
@Before 
public void setUpInput() { 
   String simulatedUserInput = "your input here"; 
   System.setIn(new ByteArrayInputStream(simulatedUserInput.getBytes())); 
} 
@After 
public void restoreSystemIn() { 
   System.setIn(originalSystemIn); 
} 
@Test 
public void testYourMethod() { 
   // Your test code here 
}
```

