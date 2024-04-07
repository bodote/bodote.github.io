---
title: "Warum TDD bei dir nicht funktioniert"
date: 2024-03-14
published: false
visible: false
categories:
  - Blog
tags:
  - TDD
toc: false
classes: wide
---

# Von TDD zu BDD

Wenn ich von Behavior Driven Development spreche, was denkst du dann?

Ich denke, es ist möglich, dass du, wenn du noch nie zuvor von BDD gehört hast, näher an der Wahrheit bist, als wenn du es hast.

## Kein Tool

Für viele Leute, die auf den Begriff BDD gestoßen sind, denken wahrscheinlich an Tools wie Cucumber und SpecFlow. Das ist ein bisschen so, als würde man an Gangschaltungen denken, wenn ich vom Auto-Fahren spreche. Diese sind Werkzeuge, die wir für BDD wählen könnten, aber sie definieren es nicht.

## Kein Prozess

Wenn du in BDD involviert warst, denkst du vielleicht an die Zusammenarbeit zwischen Menschen. Vielleicht hast du von den Drei Amigos gehört und der Wichtigkeit, zusammenzuarbeiten, um das vor uns liegende Problem zu erforschen. Ich würde argumentieren, dass diese Teil des Wertes sind, den wir sicherlich bekommen, und vielleicht Teil der Strategie, aber auch nicht wirklich den Ansatz definieren.

## Was also ist BDD und warum ist es wichtig?

Wie viele erfolgreichen Ideen, wird BDD teilweise missverstanden.   Dan North und Chris Mats bei ThoughtWorks haben versucht einen besseren Weg zu formulieren, um die Ideen, die wir in unseren Projekten als so wertvoll empfanden, zu kommunizieren und zu lehren.

### BDD um TDD leichter zugänglich  machen

Der ursprüngliche Ausgangspunkt für BDD war, einen Weg zu finden, den Menschen, die Dan, Chris und Dave in testgetriebener Entwicklung unterrichteten, schneller zum wahren Wert dieses Ansatzes zu verhelfen.

Ich glaube, dass TDD einer der größten Schritte ist, die die Softwareentwicklung unternommen hat, um unsere Praxis zu verbessern, zumindest während meiner Zeit.

TDD verstärkt das Talent eines Softwareentwicklers, indem es uns großartiges frühes Feedback über die Qualität unserer Entwürfe gibt, das keine andere Technologie oder Praxis, die ich je gesehen habe, erreichen kann.

## TDD -> missverstanden -> Probleme

Das Problem ist, dass es, wenn es missverstanden wird, in der Art und Weise, wie es oft missverstanden wird, und schlecht ausgeführt wird, den Umfang deiner Designs ändern kann, komplexe, langsame, unhandliche Tests erstellt, die eng mit deinem Code gekoppelt sind, und als Ergebnis den gesamten Entwicklungsprozess verlangsamt.

## Testing the implementation:  besser als keine TDD, aber Code schwer änderbar

Dein Code funktioniert immer noch, weil er getestet wird, aber es wird zunehmend schwieriger, ihn zu ändern.

### Sehr häufiges Fehler-Muster bei TDD Neulingen

Dieses schlechte Ergebnis ist ein sehr häufiges Muster, und wir sahen es in vielen Teams zur Zeit, als BDD erfunden wurde. Tatsächlich ist dies überhaupt nicht die Schuld von TDD. Es geht wirklich darum, dass die Leute missverstanden haben, worum es bei TDD ging, und etwas ganz anderes gemacht haben.

Also war die Idee von BDD, den Leuten zu helfen, diesen allzu häufigen Fehltritt zu vermeiden.

## TDD UNGLEICH Unit-testing UNGLEICH hohe Codeabdeckung

Der Fehler, den die Leute machten, war, dass sie testgetriebene Entwicklung mit gutem Unit-Testing verwechselten. Der große Fehler ist, dass sie annahmen, dass TDD bedeutete, Codeabdeckung in Tests zu verfolgen.

## bei richtigem TDD -> hohe Codeabdeckung ist Nebeneffekt

Wenn du TDD praktizierst, erhältst du großartige Abdeckung, aber das ist ein Nebeneffekt, kein Ziel. Und wenn du es als Ziel setzt, verpasst du den Punkt völlig und bekommst fast nie das, was du wirklich willst, nämlich die Fähigkeit, bessere Software schneller zu bauen.

## Test soll die treibende Kraft der Entwicklung sein

Testgetriebene Entwicklung ist speziell darauf ausgerichtet, den Test zuerst zu schreiben. Schließlich kannst du die Entwicklung nicht von Tests treiben, wenn du nicht mit einem Test beginnst.

Entwicklung von Tests zu treiben bedeutet, dass das Testen die treibende Kraft, der Treiber ist.

Also begannen Dan und Matt darüber nachzudenken, wie man diese Idee besser kommunizieren könnte, und der offensichtliche Ausgangspunkt war, bessere Wörter zu finden.

Es ist ziemlich offensichtlich, dass, wenn es testgetriebene Entwicklung genannt wird, es alles über das Testen geht, richtig?

## Es geht nicht nur ums Testen -> sondern großer Einfluss aufs Design

Nun, irgendwie, aber eigentlich geht es viel mehr um einen Ansatz für Design und Entwicklung, als es um das Testen geht. Die Tests sind großartig, aber der Einfluss auf Design und Entwicklung ist größer.

## Tests sind nicht nur Tests sondern Spezifikationen und Szenarien

Die Tests, die wir erstellen, sind eigentlich keine Tests, sie sind wirklich etwas anderes.

Dies ist heute immer noch ein häufiges Problem. Viele der Fragen, die ich von Leuten bekomme, wenn ich über testgetriebene Entwicklung und sogar akzeptanztestgetriebene Entwicklung spreche, handeln immer noch davon, wie wir dieses Implementierungsdetail testen sollten.

Wenn das wirklich nicht die richtige Frage ist, die man überhaupt stellen sollte.

Also hatten wir dieses Kommunikationsproblem beim Lehren von TDD, das Chris und Dan zu adressieren suchten. Ich half, eine der ersten öffentlichen Beschreibungen von BDD zu schreiben, die auf einem Wiki namens Behavior Driven.org stand. Es ist tatsächlich immer noch da, wenn du einen Blick darauf werfen möchtest, und eines der ersten Dinge, die wir schrieben, war, dass BDD darum geht, die Wörter richtig zu bekommen.

## BDD -> "Spezifikationen" und "Szenarien"

Also anstatt von Testfällen spricht BDD von Spezifikationen und anstatt von Tests spricht es von Szenarien.

Die Idee von BDD ist, dass du anfängst zu arbeiten, indem du eine Spezifikation für das erstellst, was du möchtest, dass deine Änderung an der Software hinzufügt, in Bezug auf das sichtbare Verhalten, das es aus der Sicht eines deiner Benutzer ausdrückt.

## Stoppe über deine Prod/Test-Code nachzudenken....

Das verwirrt immer noch viele Leute, aber die einfachste Art, wie ich diese Idee ausdrücken kann, ist folgende: Hör komplett auf, darüber nachzudenken, wie deine Software funktioniert.

## ... denke über die "Spezification" nach

Denke jetzt darüber nach, was deine Software aus der Sicht ihrer Benutzer tut, wer auch immer sie sein mögen. Stelle dir vor, sie kommen an den Punkt, an dem sie deine Software nutzen werden, und stelle dir nun vor, was sie erreichen wollen. Dieses Ziel, das Ding, das sie erreichen wollen, ist das, was wir in der Spezifikation erfassen wollen.

## Was "Spezifikation" NICHT ist
Ihr Ziel ist es nicht, Daten in ein Formular einzugeben oder Knöpfe zu drücken. Die Benutzeroberfläche deiner Software ist nicht das, was die Leute mit deiner Software machen wollen. Das ist nur deine Vermutung, wie sie tun können, was immer es ist, das sie tun wollen.

## einfaches Beispiel:

 *** IDEE: Zuhörer zwei Gruppen , erste Gruppe schaut 15sec den ersten test an 2. gruppe 15 den zweiten ***
Du könntest einen Test so schreiben:
```java
@Test
void test10() {
    driverPath =
            new File("/Users/bodo.teichmann/dev/learning/tddJavaMaven/chromedriver-mac-arm64/chromedriver");
    ChromeDriverService service = new ChromeDriverService.Builder()
            .usingDriverExecutable(driverPath)
            .build();
    WebDriver driver = new ChromeDriver(service);
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    try {
        driver.get("https://bodote.github.io/");
        String title = driver.getTitle();
        assertEquals("Die meisten Menschen… - Bodos Software Blog", title);
        WebElement searchLink =
                wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("fa-search")));
        searchLink.click();
        WebElement searchBox = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("search")));
        searchBox.sendKeys("TDD");
        WebElement post =
                wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText("TDD Where it did go wrong")));
        post.click();
        WebElement postHeader = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("page-title")));
        assertEquals("TDD Where it did go wrong", postHeader.getText());
        List<WebElement> foundLinks = wait.until(
                ExpectedConditions.visibilityOfAllElementsLocatedBy(By.xpath("//li//ul/li/a | //li//ol/li/a")));
        var found = foundLinks.stream().anyMatch(link -> link.getText().contains("because"));
        assertTrue(found);
    } finallvary {
        driver.quit(); // Make sure to quit the driver to free up resources
    }
}
```

Und es sagt nicht, was dieser Code tun soll.

Wenn du das genau studierst und etwas über Webentwicklung und Selenium, das Selenium-Testframework, weißt, könntest du vielleicht nach sorgfältigem Lesen herausfinden, was dieser Test tut.

Oder ich könnte den Test so schreiben, und jetzt weißt du genau, was dieser Code tun soll.

This test:
```java
@Test
void should_find_a_blog_about_TDD() {
  given().a_web_site("https://bodote.github.io/");
  when().search_menu_is_clicked().and().search_term_$_is_typed("TDD");
  then().blog_post_$_should_be_found("TDD Where it did go wrong")
          .and()
          .when_clicked_$_should_be_the_title("TDD Where it did go wrong");
}

```
Will produce this report (using `jGiven`):
```
Test Class: jgiven.BlogTest

 Should find a blog about TDD

   Given a web site "https://bodote.github.io/"
    When search menu is clicked
     And search term "TDD" is typed
    Then blog post "TDD Where it did go wrong" should be found
     And when clicked "TDD Where it did go wrong" should be the title
```

Aber jetzt hast du keine Ahnung, wie der getestete Code tatsächlich funktioniert. Du weißt nicht einmal, ob dies eine Webanwendung ist.

Nur um klar zu sein, dies sind dieselben Tests.

Der zweite Ansatz ist aus einer ganzen Reihe von Gründen viel wertvoller. Im ersten Beispiel sehen wir bereits, dass dies schwerer zu verstehen ist. Um es zu verstehen, musst du viel mehr Dinge wissen.

Du musst ein bisschen darüber wissen, wie Webseiten funktionieren, du musst wissen, was XPath ist und wie das funktioniert, und du musst ein bisschen über den Problemraum basierend auf einigen der Namen in den Labels vielleicht raten. Was ist, wenn Amazon in diesem Fall obskurere Namen verwendet hätte oder du die URL nicht erkennst?

Würdest du immer noch in der Lage sein zu sagen, was dieser Test tut?

Stell dir jetzt vor, du hättest Hunderte dieser Tests. Könntest du schnell und einfach den finden, den du suchst?

Also hat dieser Test eine Barriere zwischen den Leuten, die ihn geschrieben haben, und jedem, der ihren technischen Implementierungsdetail-fokussierten Kontext nicht teilt, gebaut.

Dies ist eine Art, wie der viel effektivere Weg, Dinge im zweiten Test zu spezifizieren, die wichtige Zusammenarbeit unterstützt, die ich am Anfang erwähnt habe.

Wir werden später darauf zurückkommen.

Das andere Problem mit dem ersten Test ist, dass er eng mit dem Code, den er testet, gekoppelt ist. Die kleinste Änderung hier macht den Test ungültig. Wenn Amazon die ID eines Labels oder die Klasse eines Div ändert, wird dieser Test brechen. Tatsächlich garantiere ich dir, wenn du diesen Test ausführst, wird er fehlschlagen, denn ich habe ihn vor einigen Jahren geschrieben, und ich wäre erstaunt, wenn Amazon ihren Code seitdem nicht geändert hätte.

Wenn ich diesen Test gegen die mobile Version oder gegen meinen Bucheinkaufsroboter ausführen möchte, ist dieser Test völlig nutzlos.

Ich müsste eine andere Version davon von Grund auf neu schreiben.

Jetzt ist es wahr, dass all diese Details irgendwo existieren müssen, damit dieser Test funktioniert, aber selbst dann, wenn ich den Test so schreibe, gibt es keine echte Wiederverwendung. Also muss jeder ähnliche Test all diese Arbeit erneut machen.

Hier ist der zweite Test wieder. Erinnere dich, dies ist derselbe Test.

Der Test konzentriert sich vollständig auf das, was der Benutzer will, das Ziel, anstatt auf den Mechanismus.

Indem wir dies tun, machen wir ihn sofort lesbar. Es ist klar für jeden, der jemals ein Buch kaufen wollte, auch wenn sie noch nie von Amazon gehört haben.

Unter diesem Code gibt es genau denselben Code, den ich dir im ersten Test gezeigt habe, aber dieses Detail ist nicht in diesen Test eingedrungen. Wenn Amazon ihre Implementierung ändert, kann ich die Verrohrung unter diesem Test ändern, ohne den Test zu ändern, und dann wird der Test wieder bestehen. Man könnte sagen, dass dies auch für den ersten Test zutrifft, aber nicht auf die gleiche Weise. Es gibt hier zwei wichtige Unterschiede.

Erstens skaliert der zweite Ansatz besser. Indem ich meine Tests so organisiere, dass sie die Zuordnung dieser domänenebene Konzepte zur Implementierungsdetail meines Systems verbergen, ist es viel offensichtlicher, dass ich diese domänenebene Abstraktionen in anderen Tests wiederverwenden kann. Viele ähnliche Tests müssen Bücher suchen oder behaupten, dass ein bestimmter Artikel in einem Einkaufskorb ist, zum Beispiel.

Also, wenn sich meine Implementierung meines Einkaufskorbs ändert, wie auch immer sie sich ändert, kann ich jetzt viele verschiedene Tests in einem einzigen Schritt reparieren.

Also ist die Wartung meiner Tests viel, viel einfacher.

Der zweite wichtige Unterschied, den ich für noch wichtiger halte, obwohl vielleicht ein bisschen subtiler, ist, dass im zweiten Beispiel, selbst wenn ich mein System unter Test auf eine Weise geändert habe, die den Test gebrochen hat, der Testfall selbst immer noch korrekt ist.

Also habe ich immer noch eine klare, genaue Aussage darüber, was mein System tun soll.

Mein Beispiel hier handelt von einem ganzen System, und ich denke, dass dies der Kontext ist, in dem die meisten Leute an BDD denken.

Aber wie ich bereits beschrieben habe, kam BDD ursprünglich nicht wirklich daher.

Es war breiter als das. Fast alles, was ich hier gesagt habe, ist gleichermaßen anwendbar, überall dort, wo wir einen Test schreiben.

Eine der hä
