# pynigma
A python shell-based Enigma simulator
Mario Seeli

######
FUNKSPRUCH
######
Um sicherzustellen, dass nicht alle Funksprüche eines Schlüsselnetzes mit identischen Schlüsseln verschlüsselt werden, was die Texte angreifbar machen würde, war vorgeschrieben, für jeden Spruch eine individuelle Anfangsstellung der drei Walzen einzustellen, „Spruchschlüssel“ genannt. Die Prozeduren hierzu änderten sich von Zeit zu Zeit und waren auch nicht bei allen Wehrmachtteilen gleichartig.[37] Bei Heer und Luftwaffe galt ab dem 1. Mai 1940[38][39] (zehn Tage vor Beginn des Westfeldzugs) das folgende in der „Schlüsselanleitung zur Schlüsselmaschine Enigma“[40] beschriebene Schema, wenn beispielsweise der folgende Klartext übermittelt werden soll:

„Das Oberkommando der Wehrmacht gibt bekannt: Aachen ist gerettet. Durch gebündelten Einsatz der Hilfskräfte konnte die Bedrohung abgewendet und die Rettung der Stadt gegen 18:00 Uhr sichergestellt werden.“

Da die Enigma nur Großbuchstaben und keine Ziffern oder Satzzeichen verschlüsseln kann und auch kein Leerzeichen kennt, muss der oben dargestellte Klartext vor der Verschlüsselung zunächst entsprechend aufbereitet werden. Dabei werden Satzzeichen durch „X“ ersetzt, Eigennamen verdoppelt und in „X“ eingeschlossen und Zahlen ziffernweise ausgeschrieben. Ferner war es üblich, (außer bei Eigennamen) das „ch“ und das „ck“ durch „Q“ zu ersetzen und den Text anschließend in Fünfergruppen aufzuteilen.[41][42] Man erhält somit den folgenden für die Verschlüsselung vorbereiteten Klartext:

DASOB ERKOM MANDO DERWE HRMAQ TGIBT BEKAN NTXAA CHENX AACHE
NXIST GERET TETXD URQGE BUEND ELTEN EINSA TZDER HILFS KRAEF
TEKON NTEDI EBEDR OHUNG ABGEW ENDET UNDDI ERETT UNGDE RSTAD
TGEGE NXEIN SXAQT XNULL XNULL XUHRS IQERG ESTEL LTWER DENX

Der Verschlüssler hat seine Enigma I, wie weiter oben beschrieben, nach dem Tagesschlüssel beispielsweise für den 31. des Monats eingestellt. (Walzenlage B I IV III, Ringstellung 16 26 08 und Steckerverbindungen AD CN ET FL GI JV KZ PU QY WX. Sowohl dieser als auch die im Folgenden beschriebenen Schritte können mithilfe frei erhältlicher Computersimulationen realitätsnah nachvollzogen werden, siehe auch: Simulationen unter Weblinks.) Der Bediener denkt sich nun eine zufällige Grundstellung aus, beispielsweise „QWE“ und stellt die drei Walzen so ein, dass genau diese drei Buchstaben in den Anzeigefenstern sichtbar werden. Nun denkt er sich einen zufälligen Spruchschlüssel, ebenfalls aus drei Buchstaben, aus, beispielsweise „RTZ“. Diesen verschlüsselt er mit seiner Enigma und beobachtet, wie nacheinander die Lampen „EWG“ aufleuchten. Den so verschlüsselten Spruchschlüssel teilt er dem Empfänger zusammen mit der zufällig gewählten Grundstellung als Indikator sowie der Uhrzeit und der Anzahl der Buchstaben des Textes als „Spruchkopf“ offen mit.

Laut damals geltender H.Dv.g.14 (= Heeres-Dienstvorschrift, geheim, Nr. 14)[43] enthält der Spruchkopf die Uhrzeit als vierstellige Zahl, die Buchstabenanzahl des Spruchs einschließlich der fünf Buchstaben der Kenngruppe sowie die gewählte Grundstellung und den verschlüsselten Spruchschlüssel (Beispiel: 2220 – 204 – qweewg). Im Allgemeinen wurden alle Buchstaben handschriftlich klein geschrieben, da sie so schneller notiert werden konnten als bei Gebrauch von Großbuchstaben. Ein authentisches Spruchformular mit dem Spruchkopf „kr – 2300 – 182 – zzxprq –“, wobei „kr“ (Abkürzung für „kriegswichtig“ oder „Kriegsnotmeldung“[44] mit dem auffälligen Morsezeichen − · −   · − ·) als Symbol für „Dringend“ steht, ist unter Weblinks als „Spruch Nr. 233“ zu sehen. Es handelt sich um eine Anfrage nach Munition für die schwere Feldhaubitze (sFH).

Als Nächstes wählt der Bediener noch drei für diesen Tag gültige Kenngruppenbuchstaben anhand einer Kenngruppentabelle aus, beispielsweise „NOW“. Die Kenngruppe hat keine kryptologische Bedeutung,[45] sie dient dem Empfänger der Nachricht nur dazu, zu erkennen, dass die Nachricht wirklich für ihn bestimmt ist und auch befugt entschlüsselt werden kann. Zur Verschleierung der Kenngruppe werden die drei Buchstaben vom Absender beliebig permutiert und um zwei für jeden Spruch zufällig zu wechselnde „Füllbuchstaben“,[46] beispielsweise „XY“, ergänzt. Aus „NOW“ wird so zunächst etwa „OWN“ und schließlich „XYOWN“. Diese fünf Buchstaben werden unverschlüsselt als erste Fünfergruppe dem Geheimtext vorangestellt.[47]

Der Verschlüssler stellt nun die drei Walzen seiner Enigma auf den von ihm gewählten Spruchschlüssel „RTZ“ ein und verschlüsselt den obigen Klartext, das heißt, er gibt jeden einzelnen Buchstaben des Klartextes über die Tastatur der Enigma ein und liest die jeweils aufleuchtende Lampe als Geheimtextbuchstaben ab und notiert ihn. Zusammen mit dem Spruchkopf und der getarnten Kenngruppe ergibt sich der folgende Funkspruch:

Kopf: 2220 – 204 – QWE EWG -
XYOWN LJPQH SVDWC LYXZQ FXHIU VWDJO BJNZX RCWEO TVNJC IONTF
QNSXW ISXKH JDAGD JVAKU KVMJA JHSZQ QJHZO IAVZO WMSCK ASRDN
XKKSR FHCXC MPJGX YIJCC KISYY SHETX VVOVD QLZYT NJXNU WKZRX
UJFXM BDIBR VMJKR HTCUJ QPTEE IYNYN JBEAQ JCLMU ODFWM ARQCF
OBWN

Kopf und Geheimtext werden als Morsezeichen gefunkt und vom Empfänger aufgenommen. Dieser prüft als erstes, ob die Anzahl der Buchstaben (hier: 204) korrekt ist und der Spruch unverstümmelt empfangen wurde. Dann betrachtet er die Kenngruppe, also die erste Fünfergruppe, ignoriert die ersten beiden Buchstaben und sieht „OWN“. Er sortiert die drei Buchstaben in alphabetischer Reihenfolge, erhält so „NOW“, schaut in seine Kenngruppentabelle, entdeckt dort diese Kenngruppenbuchstaben und kann nun sicher sein, dass der Spruch für ihn bestimmt ist und er ihn entschlüsseln kann. Seine Enigma ist bereits bezüglich Walzenlage, Ringstellung und Steckerverbindungen entsprechend dem auch ihm bekannten Tagesschlüssel identisch mit der des Absenders eingestellt. Es fehlt ihm noch der Spruchschlüssel, also die richtige Anfangsstellung der Walzen zur Entschlüsselung des Spruchs. Diese Information erhält er aus dem Indikator „QWE EWG“ im Spruchkopf, den er wie folgt interpretiert: Stelle die Walzen auf die Grundstellung „QWE“ ein und taste dann „EWG“. Nun kann er beobachten, wie nacheinander die Lampen „RTZ“ bei seiner Enigma aufleuchten. Dies ist der einzustellende Spruchschlüssel.

Er dreht nun die Walzen auf die Anfangsstellung „RTZ“ und beginnt, den Geheimtext, angefangen mit der zweiten Fünfergruppe „LJPQH“, in seine Enigma einzugeben. Nun leuchten nacheinander die Lampen auf, und der folgende Text erscheint:

dasoberkommandoderwehrmaqtgibtbekanntxaachenxaache
nxistgerettetxdurqgebuendelteneinsatzderhilfskraef
tekonntediebedrohungabgewendetunddierettungderstad
tgegenxeinsxaqtxnullxnullxuhrsiqergestelltwerdenx
