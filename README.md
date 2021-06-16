# PIR

# Contexte

Lors du deuxième semestre de 1ere année au département télécom à l'Insa Lyon, nous réalisons un projet d'initiation à la recherche. J'ai personellement choisi de réaliser le mien sur le sujet "DNS et vie privée". Le but était de reproduire des expériences d'un article scientifique : "Assessing the Privacy Benefits of Domain Name Encryption", il m'était impossible de reproduire ces expériences à l'identique mais j'ai tout de meme réussi à en reproduire quelques une à mon échelle. Je résume celle-ci dans la suite de mon écrit.

# Première expérience

On va chercher à déterminer sur une liste de 1500 noms de domaines, le nombre de domaines qui bénéficient du multi hosting. On va donc obtenir l'adresse IP de chacun de ces domaines grace à l'instruction python " socket.gethostbyname()". On va pouvoir ensuite analyser le fichier txt résultat qui nous donne les adresses ip et en ressortir le nombre de sites qui ont une adresse ip commune. On obtient que 221 sites benéficient du multi hosting ce qui représente seulement 14.7% de notre liste d'étude. Dans le papier sur lequel se base notre projet 70% des ip étaient destinées au single hosting. Les résultats semblent donc comparables.

# Deuxième expérience

Nous allons ensuite étudier la dynamisme du mapping domaine/ip, en obtenant chaque jour la liste des ip pour chacun des 1500 domaines et en la comparant à celle du jour d'avant, nous allons pouvoir déduire le pourcentage de domaines qui voient leur adresse ip changer et le fréquence de ces changements. Au bout de 1 jour 3% des domaines avaient vu leur adresse ip changer contre 15% le deuxième jour. On a ensuite 25% le 3ième jour et 63% le 4ième jour 
