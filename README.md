# Reino Cuántico - Examen CI/CD

Proyecto completo de integración continua y entrega continua (CI/CD) utilizando Flask, Docker, GitHub Actions y Traefik.

## Información del Proyecto

- **Estudiante:** Jenifer Alvarez
- **Rama de trabajo:** gonzalez
- **Imagen:** ghcr.io/jenn220/alvarez:1.0.5
- **Dominio:** https://alvarez.byronrm.com

## Estructura del Proyecto

```
jenifer-examen/
├── .github/
│   └── workflows/
│       └── cicd.yml          # Pipeline CI/CD
├── aplicacion.py              # Aplicación Flask
├── Dockerfile                 # Construcción de imagen
├── requirements.txt           # Dependencias Python
├── stack.yml                  # Configuración Docker Swarm
├── .dockerignore             # Archivos a ignorar
└── README.md                 # Este archivo
```

## Tecnologías Utilizadas

- **Flask 3.0.0** - Framework web de Python
- **Docker** - Contenedorización
- **Docker Swarm** - Orquestación
- **Traefik** - Reverse proxy con SSL automático
- **GitHub Actions** - CI/CD pipeline
- **GitHub Packages (GHCR)** - Registro de imágenes

## Pipeline CI/CD

El pipeline automáticamente:

1. **Build:** Construye la imagen Docker
2. **Publish:** Publica en GitHub Packages como `alvarez:1.0.5`
3. **Deploy:** Despliega automáticamente en el VPS sin intervención manual

### Flujo de trabajo

```
Push a rama Alvarez
    ↓
GitHub Actions ejecuta
    ↓
1. Build de imagen Docker
2. Push a ghcr.io/jenn220/alvarez:1.0.5
3. Copia stack.yml al servidor
4. Login a GHCR en el servidor
5. Pull de la imagen
6. Deploy con docker stack
    ↓
Aplicación disponible en alvarez.byronrm.com
```

## Despliegue Local

Para probar localmente:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python aplicacion.py

# Acceder a http://localhost:3000
```

## Despliegue con Docker

```bash
# Construir imagen
docker build -t alvarez:1.0.5 .

# Ejecutar contenedor
docker run -p 3000:3000 alvarez:1.0.5
```

## Configuración de Secrets

El proyecto requiere los siguientes secrets en GitHub:

- `VPS_HOST` - IP o hostname del servidor
- `VPS_USER` - Usuario SSH
- `VPS_PASSWORD` - Contraseña SSH
- `VPS_SSH_PORT` - Puerto SSH (usualmente 22)
- `GHCR_TOKEN` - Token de GitHub para acceder a packages

## Stack de Despliegue

El servicio se despliega usando Docker Swarm con:

- **Nombre del servicio:** alvarez
- **Imagen:** ghcr.io/jenn220/alvarez:1.0.5
- **Réplicas:** 1
- **Puerto interno:** 3000
- **Dominio:** alvarez.byronrm.com
- **SSL:** Automático con Let's Encrypt

## Rutas de la Aplicación

- `/` - Página principal del Reino Cuántico
- `/health` - Health check endpoint

## Monitoreo

Ver logs del servicio:

```bash
docker service logs -f alvarez_alvarez
```

Ver estado del servicio:

```bash
docker service ls | grep alvarez
```



## Autor

**Jenni Alvarez**

Examen Final - CI/CD
Fecha: Noviembre 2025