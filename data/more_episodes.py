"""
Ejemplos de Episodios para diferentes casos de uso
===================================================

Copia cualquiera de estos datasets en tu build_knowledge_graph.py
reemplazando la variable EPISODES.
"""

# ============================================================
# DATASET 1: EQUIPO DE DESARROLLO (Original - Recomendado)
# ============================================================
EPISODES_DEV_TEAM = [
    {
        "content": "Juan Pérez comenzó a trabajar como Desarrollador Senior en TechCorp el 15 de enero de 2024. Su especialidad es Python y tiene 5 años de experiencia en desarrollo backend.",
        "timestamp": "2024-01-15T09:00:00Z",
        "name": "Contratación de Juan"
    },
    {
        "content": "TechCorp es una empresa de tecnología fundada en 2018 en Buenos Aires, Argentina. Se especializa en desarrollo de software para startups y tiene 50 empleados.",
        "timestamp": "2024-01-15T10:00:00Z",
        "name": "Información de TechCorp"
    },
    {
        "content": "Juan lideró el proyecto de migración de la base de datos de PostgreSQL a MongoDB. El proyecto comenzó el 1 de febrero de 2024 y requirió 3 meses de trabajo.",
        "timestamp": "2024-02-01T09:00:00Z",
        "name": "Inicio Proyecto Migración"
    },
    {
        "content": "María García se unió al equipo de Juan como Desarrolladora Junior el 15 de febrero de 2024. Ella tiene experiencia en React y Node.js.",
        "timestamp": "2024-02-15T09:00:00Z",
        "name": "María se une al equipo"
    },
    {
        "content": "El proyecto de migración se completó exitosamente el 30 de abril de 2024. Juan y María trabajaron juntos en la implementación final.",
        "timestamp": "2024-04-30T18:00:00Z",
        "name": "Finalización del proyecto"
    },
    {
        "content": "Juan fue promovido a Tech Lead el 1 de mayo de 2024 debido a su excelente desempeño en el proyecto de migración. Su nuevo salario es de $5000 USD mensuales.",
        "timestamp": "2024-05-01T09:00:00Z",
        "name": "Promoción de Juan"
    },
    {
        "content": "TechCorp abrió una nueva oficina en Córdoba, Argentina el 15 de junio de 2024. La nueva oficina tiene capacidad para 20 empleados.",
        "timestamp": "2024-06-15T10:00:00Z",
        "name": "Nueva oficina Córdoba"
    },
    {
        "content": "María comenzó a trabajar en el proyecto de desarrollo de una API REST para clientes móviles el 1 de julio de 2024. Usa FastAPI y PostgreSQL.",
        "timestamp": "2024-07-01T09:00:00Z",
        "name": "María inicia nuevo proyecto"
    },
    {
        "content": "Juan y María asistieron a la conferencia PyConAr en Buenos Aires del 10 al 12 de agosto de 2024. Conocieron a varios desarrolladores de la comunidad Python.",
        "timestamp": "2024-08-10T09:00:00Z",
        "name": "Asistencia a PyConAr"
    },
    {
        "content": "TechCorp contrató a 10 nuevos desarrolladores en septiembre de 2024. El equipo de Juan ahora tiene 5 personas: Juan como líder, María, y tres nuevos developers junior.",
        "timestamp": "2024-09-01T09:00:00Z",
        "name": "Expansión del equipo"
    },
    {
        "content": "Juan está considerando cambiar a una empresa. Ha recibido una oferta de GlobalTech por $7000 USD mensuales. Está evaluando la propuesta durante octubre de 2024.",
        "timestamp": "2024-10-15T09:00:00Z",
        "name": "Juan evalúa nueva oferta"
    }
]


# ============================================================
# DATASET 2: PROYECTO STARTUP E-COMMERCE
# ============================================================
EPISODES_ECOMMERCE = [
    {
        "content": "ShopFast es una startup de e-commerce fundada por Laura Martínez en enero 2024. La empresa vende productos sustentables y eco-friendly en Argentina. Inversión inicial: $100,000 USD.",
        "timestamp": "2024-01-10T09:00:00Z",
        "name": "Fundación de ShopFast"
    },
    {
        "content": "Laura contrató a Pedro López como CTO de ShopFast el 15 de enero de 2024. Pedro tiene 8 años de experiencia en arquitectura de sistemas y previamente trabajó en MercadoLibre.",
        "timestamp": "2024-01-15T10:00:00Z",
        "name": "Contratación de Pedro como CTO"
    },
    {
        "content": "ShopFast lanzó su MVP (Minimum Viable Product) el 1 de febrero de 2024. La plataforma incluye catálogo de productos, carrito de compras y checkout. Stack: Next.js, Node.js, PostgreSQL.",
        "timestamp": "2024-02-01T14:00:00Z",
        "name": "Lanzamiento del MVP"
    },
    {
        "content": "En la primera semana, ShopFast logró 50 ventas con un ticket promedio de $2,500 pesos argentinos. Los productos más vendidos fueron botellas reutilizables y bolsas de tela.",
        "timestamp": "2024-02-08T18:00:00Z",
        "name": "Primeras métricas de ventas"
    },
    {
        "content": "ShopFast cerró una ronda seed de inversión de $500,000 USD con el fondo SeedVC Argentina el 1 de marzo de 2024. Los inversores principales son Martín Rodríguez y Ana Fernández.",
        "timestamp": "2024-03-01T11:00:00Z",
        "name": "Ronda Seed de inversión"
    },
    {
        "content": "Con la nueva inversión, Laura contrató un equipo de 5 personas: 2 developers, 1 diseñador UX/UI, 1 marketing manager y 1 customer success. El equipo total ahora es de 7 personas.",
        "timestamp": "2024-03-15T09:00:00Z",
        "name": "Expansión del equipo"
    },
    {
        "content": "Pedro implementó un sistema de recomendaciones usando machine learning con scikit-learn. El sistema analiza el comportamiento de compra y sugiere productos relacionados.",
        "timestamp": "2024-04-01T10:00:00Z",
        "name": "Sistema de recomendaciones ML"
    },
    {
        "content": "ShopFast alcanzó 1,000 clientes registrados y 500 ventas mensuales en abril 2024. El revenue mensual es de $1,250,000 pesos argentinos (~$1,500 USD al tipo de cambio).",
        "timestamp": "2024-04-30T23:59:00Z",
        "name": "Milestone 1K clientes"
    },
    {
        "content": "Laura y Pedro asistieron a un evento de networking de startups en Buenos Aires el 15 de mayo 2024. Conocieron a inversores de USA y Europa interesados en el modelo de negocio sustentable.",
        "timestamp": "2024-05-15T16:00:00Z",
        "name": "Networking con inversores"
    },
    {
        "content": "ShopFast expandió su catálogo a 200 productos de 30 proveedores locales el 1 de junio 2024. Se agregaron categorías nuevas: cosmética natural, ropa sustentable y productos para el hogar.",
        "timestamp": "2024-06-01T09:00:00Z",
        "name": "Expansión del catálogo"
    },
    {
        "content": "Pedro está evaluando migrar la infraestructura de Vercel a AWS para reducir costos. El gasto actual en Vercel es de $800 USD mensuales y en AWS sería $400 USD con mayor escalabilidad.",
        "timestamp": "2024-07-10T14:00:00Z",
        "name": "Evaluación migración a AWS"
    },
]


# ============================================================
# DATASET 3: INVESTIGACIÓN CIENTÍFICA - COVID-19
# ============================================================
EPISODES_COVID_RESEARCH = [
    {
        "content": "El Dr. Carlos Méndez del Instituto de Virología de Buenos Aires comenzó un estudio sobre variantes de COVID-19 en enero 2024. El equipo tiene 8 investigadores y cuenta con financiamiento del CONICET.",
        "timestamp": "2024-01-05T08:00:00Z",
        "name": "Inicio estudio variantes COVID"
    },
    {
        "content": "Se identificó una nueva subvariante de Ómicron denominada BA.2.86.1 en muestras de Buenos Aires el 15 de enero 2024. La subvariante muestra 12 mutaciones adicionales en la proteína spike.",
        "timestamp": "2024-01-15T16:30:00Z",
        "name": "Detección BA.2.86.1"
    },
    {
        "content": "La Dra. Ana Rodríguez se unió al equipo como especialista en secuenciación genómica el 1 de febrero 2024. Ella completó su postdoctorado en el MIT y tiene experiencia en CRISPR.",
        "timestamp": "2024-02-01T09:00:00Z",
        "name": "Incorporación Dra. Rodríguez"
    },
    {
        "content": "El equipo secuenció 150 muestras de pacientes usando tecnología Illumina NovaSeq. Los resultados muestran que BA.2.86.1 representa el 23% de los casos en Buenos Aires al 15 de febrero 2024.",
        "timestamp": "2024-02-15T18:00:00Z",
        "name": "Secuenciación 150 muestras"
    },
    {
        "content": "Se publicó un preprint en medRxiv el 1 de marzo 2024 con los hallazgos del equipo. El paper recibió 45 citaciones en las primeras dos semanas y atención de medios internacionales.",
        "timestamp": "2024-03-01T10:00:00Z",
        "name": "Publicación preprint medRxiv"
    },
    {
        "content": "El Dr. Méndez presentó los resultados en una conferencia virtual de la OMS el 15 de marzo 2024. Asistieron 300 investigadores de 45 países. La presentación fue muy bien recibida.",
        "timestamp": "2024-03-15T14:00:00Z",
        "name": "Presentación OMS virtual"
    },
    {
        "content": "La Dra. Rodríguez desarrolló un modelo computacional para predecir futuras mutaciones usando machine learning. El modelo usa PyTorch y fue entrenado con 10,000 secuencias genómicas.",
        "timestamp": "2024-04-01T11:00:00Z",
        "name": "Modelo predictivo ML"
    },
    {
        "content": "El equipo recibió una grant adicional de $200,000 USD de la fundación Bill & Melinda Gates el 15 de abril 2024 para continuar la investigación por 2 años más.",
        "timestamp": "2024-04-15T09:00:00Z",
        "name": "Grant Gates Foundation"
    },
    {
        "content": "Se estableció una colaboración con la Universidad de Oxford el 1 de mayo 2024. El intercambio incluye muestras, datos y dos investigadores visitantes por 6 meses.",
        "timestamp": "2024-05-01T10:00:00Z",
        "name": "Colaboración con Oxford"
    },
    {
        "content": "El paper fue aceptado en Nature Medicine el 15 de junio 2024 tras peer review. Es la primera publicación argentina en esta revista sobre COVID-19. Factor de impacto: 87.2.",
        "timestamp": "2024-06-15T15:30:00Z",
        "name": "Aceptación Nature Medicine"
    },
    {
        "content": "El Dr. Méndez fue nominado al premio Konex 2024 en la categoría Virología por sus contribuciones al entendimiento de las variantes de COVID-19.",
        "timestamp": "2024-07-20T12:00:00Z",
        "name": "Nominación Premio Konex"
    },
]


# ============================================================
# DATASET 4: CLUB DE FÚTBOL - GESTIÓN DEPORTIVA
# ============================================================
EPISODES_FOOTBALL_CLUB = [
    {
        "content": "El Club Atlético Independiente contrató a Marcelo Gallardo como director técnico el 1 de enero 2024. Contrato por 2 años con salario de $500,000 USD anuales. Gallardo venía de dirigir River Plate.",
        "timestamp": "2024-01-01T10:00:00Z",
        "name": "Contratación Gallardo DT"
    },
    {
        "content": "Independiente fichó al delantero brasileño Lucas Silva por $8 millones de USD el 15 de enero 2024. Silva tiene 24 años, venía del Flamengo y firmó por 4 años.",
        "timestamp": "2024-01-15T14:00:00Z",
        "name": "Fichaje Lucas Silva"
    },
    {
        "content": "En el primer partido del torneo el 28 de enero 2024, Independiente venció a Boca Juniors 2-1. Lucas Silva anotó su primer gol con la camiseta roja. Asistieron 45,000 espectadores.",
        "timestamp": "2024-01-28T21:30:00Z",
        "name": "Victoria vs Boca 2-1"
    },
    {
        "content": "El preparador físico Juan Martínez implementó un nuevo sistema de análisis de datos con GPS para monitorear el rendimiento físico de los jugadores. Se usa el software Catapult Sports.",
        "timestamp": "2024-02-05T09:00:00Z",
        "name": "Sistema GPS tracking"
    },
    {
        "content": "Independiente perdió 0-3 contra San Lorenzo el 15 de febrero 2024. Fue la primera derrota bajo la dirección de Gallardo. El equipo mostró problemas defensivos.",
        "timestamp": "2024-02-15T21:00:00Z",
        "name": "Derrota vs San Lorenzo"
    },
    {
        "content": "El club fichó al defensor central argentino Rodrigo López por $3 millones de USD el 1 de marzo 2024 para reforzar la defensa. López venía de Estudiantes y tiene experiencia en libertadores.",
        "timestamp": "2024-03-01T11:00:00Z",
        "name": "Fichaje Rodrigo López defensa"
    },
    {
        "content": "Lucas Silva sufrió una lesión en el ligamento cruzado anterior durante el entrenamiento el 10 de marzo 2024. Estará fuera por 6-8 meses. Gran golpe para el equipo.",
        "timestamp": "2024-03-10T16:00:00Z",
        "name": "Lesión Lucas Silva LCA"
    },
    {
        "content": "Independiente clasificó a los octavos de final de la Copa Libertadores el 15 de abril 2024 tras vencer 2-0 a Palmeiras en Brasil. Rodrigo López fue figura con un gol.",
        "timestamp": "2024-04-15T22:00:00Z",
        "name": "Clasificación Libertadores"
    },
    {
        "content": "El club firmó un nuevo sponsor principal con Coca-Cola por $5 millones de USD anuales el 1 de mayo 2024. Es el contrato más grande de la historia del club.",
        "timestamp": "2024-05-01T10:00:00Z",
        "name": "Sponsor Coca-Cola"
    },
    {
        "content": "Independiente está en el primer lugar del torneo local con 35 puntos en 15 partidos al 30 de mayo 2024. El sistema táctico 4-3-3 de Gallardo está funcionando muy bien.",
        "timestamp": "2024-05-30T23:59:00Z",
        "name": "Liderazgo tabla torneo"
    },
    {
        "content": "Lucas Silva comenzó su rehabilitación con el equipo médico el 1 de junio 2024. Los estudios muestran buena evolución. Se espera que vuelva a entrenar en agosto.",
        "timestamp": "2024-06-01T09:00:00Z",
        "name": "Inicio rehabilitación Silva"
    },
]


# ============================================================
# DATASET 5: RESTAURANTE Y GASTRONOMÍA
# ============================================================
EPISODES_RESTAURANT = [
    {
        "content": "Sofía Martínez inauguró el restaurante 'Sabores Porteños' en Palermo el 10 de enero 2024. Especialidad: cocina argentina contemporánea. Inversión inicial: $150,000 USD. Capacidad: 60 comensales.",
        "timestamp": "2024-01-10T19:00:00Z",
        "name": "Inauguración restaurante"
    },
    {
        "content": "Contrató al chef Diego Fernández como chef ejecutivo el 5 de enero 2024. Diego trabajó 5 años en el restaurante Don Julio (top 50 mundial). Salario: $4,000 USD mensuales.",
        "timestamp": "2024-01-05T10:00:00Z",
        "name": "Contratación Chef Diego"
    },
    {
        "content": "El restaurante recibió una crítica muy positiva en La Nación el 25 de enero 2024. El periodista gastronómico Pablo Castro le dio 4/5 estrellas. Destacó el bife de chorizo y el postre de dulce de leche.",
        "timestamp": "2024-01-25T08:00:00Z",
        "name": "Crítica positiva La Nación"
    },
    {
        "content": "En febrero 2024, el ticket promedio fue de $15,000 pesos argentinos por persona. Se sirvieron 1,200 comensales. Los ingresos del mes fueron de $18 millones de pesos.",
        "timestamp": "2024-02-29T23:59:00Z",
        "name": "Métricas febrero 2024"
    },
    {
        "content": "Diego creó un nuevo menú degustación de 7 pasos el 1 de marzo 2024. Precio: $35,000 pesos. Incluye maridaje con vinos argentinos de Mendoza. Se ofrece viernes y sábados.",
        "timestamp": "2024-03-01T12:00:00Z",
        "name": "Menú degustación nuevo"
    },
    {
        "content": "Sabores Porteños apareció en la guía Michelin Argentina 2024 el 15 de marzo. Recibió mención Bib Gourmand (buena relación calidad-precio). Primer reconocimiento internacional.",
        "timestamp": "2024-03-15T09:00:00Z",
        "name": "Bib Gourmand Michelin"
    },
    {
        "content": "Se implementó un sistema de reservas online con TheFork el 1 de abril 2024. Las reservas aumentaron 40%. El restaurante ahora opera al 85% de capacidad promedio.",
        "timestamp": "2024-04-01T10:00:00Z",
        "name": "Sistema reservas TheFork"
    },
    {
        "content": "Diego viajó a España para una colaboración con el restaurante DiverXO (3 estrellas Michelin) del 10 al 17 de mayo 2024. Aprendió nuevas técnicas de cocina molecular.",
        "timestamp": "2024-05-10T08:00:00Z",
        "name": "Colaboración DiverXO España"
    },
    {
        "content": "Sofía abrió una segunda locación del restaurante en Recoleta el 1 de junio 2024. Inversión: $200,000 USD. El nuevo chef es Martín Ríos, ex sous-chef de la locación original.",
        "timestamp": "2024-06-01T19:00:00Z",
        "name": "Apertura Recoleta segunda locación"
    },
    {
        "content": "Sabores Porteños firmó un contrato con Rappi para delivery el 15 de junio 2024. Se creó un menú especial para delivery. Las ventas de delivery representan el 20% del total.",
        "timestamp": "2024-06-15T11:00:00Z",
        "name": "Lanzamiento delivery Rappi"
    },
    {
        "content": "El restaurante ganó el premio 'Mejor Restaurante Nuevo 2024' de la Cámara de Restaurantes y Bares de Buenos Aires el 30 de junio 2024. Premio muy prestigioso en el sector gastronómico.",
        "timestamp": "2024-06-30T20:00:00Z",
        "name": "Premio Mejor Restaurante Nuevo"
    },
]


# ============================================================
# INSTRUCCIONES DE USO
# ============================================================
"""
Para usar cualquiera de estos datasets:

1. Abre build_knowledge_graph.py
2. Reemplaza la variable EPISODES con el dataset que quieras:
   
   # Opción 1: Equipo de desarrollo
   EPISODES = EPISODES_DEV_TEAM
   
   # Opción 2: Startup e-commerce
   EPISODES = EPISODES_ECOMMERCE
   
   # Opción 3: Investigación COVID
   EPISODES = EPISODES_COVID_RESEARCH
   
   # Opción 4: Club de fútbol
   EPISODES = EPISODES_FOOTBALL_CLUB
   
   # Opción 5: Restaurante
   EPISODES = EPISODES_RESTAURANT

3. Ejecuta: python build_knowledge_graph.py
"""