# Contenido de la demo Palma Riad (Palma) (es/ca/en/fr). Hechos de palmariad.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las suites reales.','ca':' Les imatges són il·lustracions i no mostren les suites reals.','en':' Images are illustrations and do not show the actual suites.','fr':' Les images sont des illustrations et ne montrent pas les suites réelles.'}
H={'es':['Suite Alhambra','Suite Yasmine','Suite Sultán'],'ca':['Suite Alhambra','Suite Yasmine','Suite Sultán'],'en':['Suite Alhambra','Suite Yasmine','Suite Sultán'],'fr':['Suite Alhambra','Suite Yasmine','Suite Sultán']}
RD={
'es':['46 m² abuhardillados con salón, gran baño con ducha y bañera separadas y cama extragrande.','31 m² más terraza de 10 m² con cama balinesa y vistas al patio; bañera estilo cueva.','La joya de la casa: 70 m² con salón separado del dormitorio, para hasta 4 adultos.'],
'ca':['46 m² amb golfes, saló, gran bany amb dutxa i banyera separades i llit extragran.','31 m² més terrassa de 10 m² amb llit balinès i vistes al pati; banyera estil cova.','La joia de la casa: 70 m² amb saló separat del dormitori, per a fins a 4 adults.'],
'en':['46 m² under a mansard roof, with a living room, a huge bathroom with separate shower and bathtub, and an extra-large bed.','31 m² plus a 10 m² terrace with a Balinese bed and patio views; cave-style bathtub.','The jewel of the crown: 70 m² with a living room separate from the bedroom, for up to 4 adults.'],
'fr':['46 m² mansardés avec salon, grande salle de bain avec douche et baignoire séparées et lit très grand.','31 m² plus une terrasse de 10 m² avec lit balinais et vue sur le patio ; baignoire style grotte.','Le joyau de la maison : 70 m² avec salon séparé de la chambre, pour 4 adultes maximum.']}
ART={
'hero':('arches',6101,['#f6ead9','#e9c28f','#b8693a','#2f5d55','#1b3a35']),
'intro':('columns',6102,['#f4ece0','#faf3ea','#c4903f','#2f5d55','#1b3a35']),
'r1':('arches',6111,['#f5e8d6','#e6be8a','#b4643a','#2f5d55','#1b3a35']),
'r2':('columns',6112,['#f3eadf','#f9f2e8','#c88f42','#2f5d55','#1b3a35']),
'r3':('skyline',6113,['#2f5d55','#e2975c','#f6d39c','#2c5850','#21443e','#152d29']),
'g1':('arches',6121,['#f6eadb','#e8c190','#bb6b3b','#7a3a22','#4a2414']),
'g2':('columns',6122,['#f2e9de','#f8f0e6','#c28b3e','#2f5d55','#1b3a35']),
'g3':('skyline',6123,['#33625a','#e69a5e','#f8d7a2','#305e56','#24483f','#17302b']),
'g4':('hills',6124,['#eee6cf','#f4e3bf','#f3c987','#b6c39b','#8ca482','#607a63']),
'g5':('arches',6125,['#f5e7d6','#e4bb88','#b66a38','#7a3a22','#4a2414']),
'g6':('columns',6126,['#f1e8dc','#f8efe5','#bf8840','#2f5d55','#1b3a35'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Palma Riad · Hotel 5 estrellas solo para adultos en el centro de Palma',see_rooms='Ver suites',hero_k='Palma · Casco antiguo',hero_t='Un riad en el corazón de Palma',hero_s='Hotel de 5 estrellas solo para adultos con 11 suites, en la calle Sant Jaume, 5.',
 intro_t='Inspirado en los riads de Marruecos',intro_p1='Palma Riad nace para revivir el legado de Madina Mayurqa: una casa escondida alrededor de un patio, donde el tiempo va más despacio.',
 intro_p2='11 suites, cada una única y original, que unen Mallorca y Marruecos, a pocos pasos de los principales puntos de interés, las mejores tiendas y los mejores restaurantes.',
 stats=['11 suites','5 estrellas','Solo adultos','Desayuno incluido'],nav_rooms='Suites',rooms_t='Suites',rooms_s='Once suites distintas; aquí tienes tres de ellas.',
 svcs=['Desayuno incluido','Cocktail bar','Solárium con tumbonas','Wifi de alta velocidad','Aire acondicionado y calefacción','Habitaciones insonorizadas','Cafetera Nespresso y minibar gourmet','Amenities Molton Brown'],
 loc_p='Carrer de Sant Jaume, 5 · 07012 Palma (Illes Balears). El hotel no tiene parking propio; recomienda los aparcamientos públicos cercanos.',
 chips=['¿Qué suites tiene?','¿El desayuno está incluido?','¿Hay parking?','¿Cómo se reserva?']),
'ca':dict(title='Palma Riad · Hotel 5 estrelles només per a adults al centre de Palma',see_rooms='Veure suites',hero_k='Palma · Nucli antic',hero_t='Un riad al cor de Palma',hero_s='Hotel de 5 estrelles només per a adults amb 11 suites, al carrer de Sant Jaume, 5.',
 intro_t='Inspirat en els riads del Marroc',intro_p1='Palma Riad neix per reviure el llegat de Madina Mayurqa: una casa amagada al voltant d\'un pati, on el temps va més a poc a poc.',
 intro_p2='11 suites, cadascuna única i original, que uneixen Mallorca i el Marroc, a poques passes dels principals punts d\'interès, les millors botigues i els millors restaurants.',
 stats=['11 suites','5 estrelles','Només adults','Esmorzar inclòs'],nav_rooms='Suites',rooms_t='Suites',rooms_s='Onze suites diferents; aquí en tens tres.',
 svcs=['Esmorzar inclòs','Cocktail bar','Solàrium amb gandules','Wifi d\'alta velocitat','Aire condicionat i calefacció','Habitacions insonoritzades','Cafetera Nespresso i minibar gurmet','Amenities Molton Brown'],
 loc_p='Carrer de Sant Jaume, 5 · 07012 Palma (Illes Balears). L\'hotel no té pàrquing propi; recomana els aparcaments públics propers.',
 chips=['Quines suites té?','L\'esmorzar està inclòs?','Hi ha pàrquing?','Com es reserva?']),
'en':dict(title='Palma Riad · 5-star adults-only hotel in the centre of Palma',see_rooms='See the suites',hero_k='Palma · Old town',hero_t='A riad in the heart of Palma',hero_s='A 5-star adults-only hotel with 11 suites, at Carrer de Sant Jaume, 5.',
 intro_t='Inspired by the riads of Morocco',intro_p1='Palma Riad was born to revive the legacy of Madina Mayurqa: a hidden house built around a courtyard, where time slows down.',
 intro_p2='11 suites, each unique and original, connecting Mallorca and Morocco, a few steps from the main sights, the best shops and top restaurants.',
 stats=['11 suites','5 stars','Adults only','Breakfast included'],nav_rooms='Suites',rooms_t='Suites',rooms_s='Eleven different suites; here are three of them.',
 svcs=['Breakfast included','Cocktail bar','Solarium with sun loungers','High-speed wifi','Air conditioning and heating','Soundproof rooms','Nespresso machine and gourmet minibar','Molton Brown amenities'],
 loc_p='Carrer de Sant Jaume, 5 · 07012 Palma (Illes Balears). The hotel has no parking of its own; it recommends the nearby public car parks.',
 chips=['What suites are there?','Is breakfast included?','Is there parking?','How do I book?']),
'fr':dict(title='Palma Riad · Hôtel 5 étoiles réservé aux adultes au centre de Palma',see_rooms='Voir les suites',hero_k='Palma · Vieille ville',hero_t='Un riad au cœur de Palma',hero_s='Hôtel 5 étoiles réservé aux adultes avec 11 suites, Carrer de Sant Jaume, 5.',
 intro_t='Inspiré des riads du Maroc',intro_p1='Palma Riad est né pour faire revivre l\'héritage de Madina Mayurqa : une maison cachée autour d\'un patio, où le temps ralentit.',
 intro_p2='11 suites, toutes uniques et originales, qui relient Majorque et le Maroc, à quelques pas des principaux sites, des meilleures boutiques et des meilleurs restaurants.',
 stats=['11 suites','5 étoiles','Adultes uniquement','Petit-déjeuner inclus'],nav_rooms='Suites',rooms_t='Suites',rooms_s='Onze suites différentes ; en voici trois.',
 svcs=['Petit-déjeuner inclus','Bar à cocktails','Solarium avec transats','Wifi haut débit','Climatisation et chauffage','Chambres insonorisées','Machine Nespresso et minibar gourmet','Produits Molton Brown'],
 loc_p='Carrer de Sant Jaume, 5 · 07012 Palma (Illes Balears). L\'hôtel n\'a pas de parking ; il recommande les parkings publics proches.',
 chips=['Quelles suites y a-t-il ?','Le petit-déjeuner est-il inclus ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES_ES='https://reservations.palmariad.com/palmariad.com/es/availability'; RES_EN='https://reservations.palmariad.com/palmariad.com/en/availability'
BOOK=dict(mode='engine',url={'es':RES_ES,'ca':RES_ES,'en':RES_EN,'fr':RES_EN})
D=dict(name='Palma Riad',ac='#2f5d55',ac2='#b8693a',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='Carrer de Sant Jaume, 5 · 07012 Palma',phones=['+34 871 871 210'],emails=['reservations@palmariad.com'],maps='Palma Riad, Carrer de Sant Jaume 5, Palma',t=T)
META=dict(repo='demo-palma-riad-palma',name='Palma Riad',legal_name='Comercial Ramis, S.L.',registry_ids=['CIF B07041783','Registro Mercantil de Palma hoja PM-7151','Registro turístico H/3019'],
 url='https://palmariad.com/',domain='palmariad.com',municipality='Palma',province='Illes Balears',sector='hotel boutique de 5 estrellas solo para adultos en el centro de Palma',
 read_at='2026-10-29T11:06:00+01:00',created_at='2026-10-29T11:05:00+01:00',built_at='2026-10-29T11:15:00+01:00',audit_date='2026-10-29T11:05:18+01:00',
 rating=dict(value=4.8,coincide=['telefono','web','direccion'],date='2026-10-29T10:36:12+01:00',url='https://www.google.com/maps/place/Palma+Riad/@39.572062,2.6472883,17z/data=!4m9!3m8!1s0x1297925aed86c1f3:0xc86bae52c8b42794!5m2!4m1!1i2!8m2!3d39.572062!4d2.6472883!16s%2Fg%2F11rc4my1ht'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas real del hotel (reservations.palmariad.com, enlazado desde el boton «Book/Reservar» de su web); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué suites tiene?','K01'),('¿Cuál es la suite más grande?','K02'),('¿El desayuno está incluido?','K03'),('¿Hay parking?','K04'),('¿Pueden venir niños?','K05'),('¿Dónde está el hotel?','K06'),('¿Tienen cocktail bar?','K07'),('¿Qué tiene la suite?','K08'),('¿A qué hora es la entrada?','K09'),('¿Cómo reservo?','K10'),('¿Admiten mascotas?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una suite libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines suites té?','K01'),('Quina és la suite més gran?','K02'),('L\'esmorzar està inclòs?','K03'),('Hi ha pàrquing?','K04'),('Hi poden venir nens?','K05'),('On és l\'hotel?','K06'),('Teniu cocktail bar?','K07'),('Què té la suite?','K08'),('A quina hora és l\'entrada?','K09'),('Com reservo?','K10'),('Admeteu mascotes?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una suite lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What suites are there?','K01'),('Which is the largest suite?','K02'),('Is breakfast included?','K03'),('Is there parking?','K04'),('Can children come?','K05'),('Where is the hotel?','K06'),('Do you have a cocktail bar?','K07'),('What does the suite include?','K08'),('What time is check-in?','K09'),('How do I book?','K10'),('Are pets allowed?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free suite tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles suites y a-t-il ?','K01'),('Quelle est la plus grande suite ?','K02'),('Le petit-déjeuner est-il inclus ?','K03'),('Y a-t-il un parking ?','K04'),('Les enfants peuvent-ils venir ?','K05'),('Où est l\'hôtel ?','K06'),('Avez-vous un bar à cocktails ?','K07'),('Qu\'y a-t-il dans la suite ?','K08'),('À quelle heure est l\'arrivée ?','K09'),('Comment réserver ?','K10'),('Les animaux sont-ils admis ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une suite libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
