# Ch-akiSoft

## Instrucciones de Instalaciónn

1. Requisitos
  Python 3.x
  pip (gestor de paquetes de Python)

2. Instalación del plugin de Allure
Primero, necesitas instalar el plugin de Pytest que permite generar los archivos de reporte de Allure.

```
pip install allure-pytest
```

3. Instalación de Allure Commandline
Para generar los reportes HTML, necesitas tener la herramienta de línea de comandos de Allure instalada en tu sistema.

En Windows (usando PowerShell y Scoop):
Si no tienes Scoop, primero instálalo con los siguientes comandos:

PowerShell
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

Luego, instala Allure:

```
scoop install allure
```

Puedes verificar la instalación ejecutando:

```
allure --version
```

4. Ejecución de pruebas y generación de reportes
Una vez que el plugin y la herramienta de Allure están instalados, puedes ejecutar tus pruebas y generar el reporte.

Ejecuta tus pruebas con Pytest, indicando la carpeta donde se guardarán los resultados. La bandera --alluredir es obligatoria.

```
pytest
```
Esto creará una carpeta llamada reports (puedes nombrarla como quieras) con los archivos de resultados.

Genera y visualiza el reporte HTML. Este comando tomará los archivos de la carpeta reports y creará un reporte visual que se abrirá automáticamente en tu navegador.

```
allure serve reports
```

### Comandos para ejecutar pruebas

#### Feature

* Attachments
  ```
  pytest tests/api-qase/attachments
  ```
* Cases
   ```
  pytest tests/api-qase/Cases
  ```
* Custom_Field
  ```
  pytest tests/api-qase/Custom_Field
  ```
* plan
   ```
  pytest tests/api-qase/plan
  ```
* Project
   ```
  pytest tests/api-qase/Project
  ```
* Suite
   ```
  pytest tests/api-qase/suite
  ```
#### Tipo de Prueba

* Smoke
  ```
  pytest -m "smoke"
  ```
* Negative
   ```
  pytest -m "negative"
  ```
* Positive
  ```
  pytest -m "positive"
  ```
* Regression
   ```
  pytest -m "regression"
  ```        

## Test Plan

### Nombre del plan: Test Plan – Qase
#### Versión: 1.0

1. Descripción del producto

Qase es una plataforma en línea especializada en la gestión integral de pruebas de software. Está diseñada para equipos de desarrollo y aseguramiento de calidad (QA) que buscan optimizar su flujo de trabajo y garantizar que cada funcionalidad de un producto sea validada antes de su lanzamiento. Al ser una herramienta basada en la web, no requiere instalaciones complejas y puede utilizarse desde cualquier navegador, facilitando así la colaboración entre equipos distribuidos.
Qase funciona como un repositorio central donde se crean, organizan y mantienen actualizados los casos de prueba. Cada caso incluye instrucciones detalladas para verificar una funcionalidad específica, definiendo objetivos, pasos a seguir y resultados esperados.
Una de las funciones más importantes de Qase es la ejecución y seguimiento de pruebas en tiempo real. Los testers pueden registrar los resultados obtenidos, reportar errores y documentar evidencias como capturas de pantalla o notas técnicas. Además, la plataforma ofrece un sistema integrado para la gestión de defectos, que permite asignar responsabilidades, priorizar incidencias y dar seguimiento a cada error hasta su resolución.
En cuanto a análisis y métricas, Qase ofrece reportes detallados y paneles de control que muestran indicadores clave como el avance de las pruebas, la cobertura alcanzada y el número de defectos detectados. Estos datos ayudan a tomar decisiones estratégicas y a identificar áreas de mejora en el proceso de validación del producto.
Qase centraliza la gestión de pruebas, mejora la comunicación interna, evita la omisión de validaciones críticas y agiliza el trabajo mediante la automatización. Su interfaz intuitiva y estructura clara permiten que incluso quienes no tienen experiencia previa en test management puedan utilizarla de manera efectiva, convirtiéndola en una herramienta esencial para garantizar la calidad y confiabilidad de cualquier software.
** ¿Por qué sería importante testearlo? ** 
Escogimos Qase porque nosotros al ser QA requerimos de esta aplicación como herramienta cotidiana y por tanto es requerida su funcionalidad con la menor cantidad de errores
Testear Qase es una prioridad absoluta porque la calidad de un producto de software es un reflejo directo de la calidad de las herramientas utilizadas para validarlo. Si la propia herramienta de QA falla, el proceso de aseguramiento de la calidad queda en entredicho. Es una responsabilidad crucial que la herramienta que usamos para garantizar la calidad en otros productos, sea de la más alta calidad posible.
La primera y principal razón es que los usuarios de Qase (equipos de QA y desarrolladores) dependen de la herramienta para gestionar sus procesos de prueba. Si la plataforma tiene errores, se vuelve poco confiable. Un error en la herramienta de gestión de pruebas podría, por ejemplo, perder datos de casos de prueba, borrar resultados de ejecución o fallar al generar informes. Esto podría llevar a que los equipos pierdan la confianza en Qase y busquen una alternativa.

2. Funcionalidades
Como equipo, determinamos escoger estas funcionalidades debido a la cantidad  de  métodos HTTP que ofrecen  de la API de Qase

** Attachments ** 
Permite ver los archivos existentes, subir  archivos (como imágenes o documentos), buscar un archivo en especifico y eliminar un archivo en especifico.

	1. Obtener todo los archivos adjuntos 
		Permite listar una determinada cantidad de archivos y también omitir cierta cantidad de archivos con 
		Limit
		offset 





Estrategia 
Exploratory Testing: Se empleara esta técnica para explorar y comprender el comportamiento general de la aplicación, identificando posibles áreas de interés o problemas no documentados.

Smoke Testing: Consiste en verificar que la API responda correctamente a las solicitudes básicas positiva code 200, asegurando que los componentes principales funcionen antes de realizar pruebas más exhaustivas.

Functional Testing: Se valida que cada endpoint cumpla con su propósito y entregue los resultados esperados, asegurando el correcto funcionamiento según los requerimientos.

Regression Testing: Se ejecutan pruebas para confirmar que los cambios o actualizaciones realizadas no afecten ni deterioren las funcionalidades previamente implementadas. 
Se aplicarán a todos los test case 

Funcional Negativo: Se valida que el sistema maneje los errores de manera adecuada y permita observar el mensaje de error

Alcance y Limitaciones
El presente plan de pruebas está enfocado en la validación funcional de los módulos workspace y project de Qase, con sus submódulos (Attachments, Cases,
Custom Fields, Projects, Suites) 


Funcionalidades a ser Probadas:
El proyecto consta de 20 endpoints pertenecientes a los módulos: Attachments, Cases, Custom Fields, Projects, Suites.
1er Sprint
Para este primer Sprint se contemplaran 10 endpoints de los cuales:
Diego Armando Lomar Jain
Asignado al módulo “Workspace” estará encargado de implementar y validar el siguiente endpoint dentro del submódulo “Attachment” (GET ALL , POST, GET):
Obtener todos los archivos adjuntos 
Subir archivo adjunto
Obtener archivo adjunto en específico
También asignado al módulo “Project” estará encargado de implementar y validar el siguiente endpoint dentro del submódulo “Cases” (POST)
Adjuntar los problemas externos a los casos de prueba
Gualberto Choque Choque
Asignado al módulo “Project” estará encargado de implementar y validar los siguientes endpoints (GET ALL , POST):
Obtener todos los proyectos
Crear nuevo proyecto
David Gregori Rodriguez Calle
Asignado al módulo “Project” estará encargado de implementar y validar los siguientes endpoints dentro del submódulo “Cases” (GET ALL , POST,GET)
Obtener todos los casos de prueba de un proyecto.
Crear un nuevo caso de prueba.
Andres Adrian Estrada Uzeda
Asignado al módulo “Workspace”estará encargado de implementar y validar los siguientes endpoints dentro del submodulo “Custom Fields” (  POST,GET)
Crear nuevo campo personalizado
Obtener campo personalizado por ID

                        Sol Abril Marquez Diaz
Asignada al módulo “Suites”, estará a cargo de implementar y validar los siguientes endpoints (GET, POST)
Obtener todos los suite de prueba
Crear un nuevo suite 
2do Sprint
Para este primer Sprint se contemplaran 10 endpoints de los cuales:
Diego Armando Lomar Jain
Asignado al módulo “Workspace” estará encargado de implementar y validar el siguiente endpoint dentro del submódulo “Attachment” (DELETE):
Eliminar archivo adjunto en específico 
David Gregori Rodriguez Calle
Asignado al módulo “Proyect” estará encargado de implementar y validar los siguientes endpoints dentro del submódulo “Cases” (POST, DELETE, PATCH)
Actualizar un caso de prueba existente.
Obtener un caso de prueba específico por su ID.
Eliminar un caso de prueba por su ID.
Andres Adrian Estrada Uzeda
Asignado al módulo “Workspace”estará encargado de implementar y validar los siguientes endpoints dentro del submodulo “Custom Fields” ( DELETE,PATCH)
Eliminar campo personalizado por ID
Actualizar campo personalizado por ID

                         Sol Abril Marquez Diaz
Asignada al módulo “Suites”, estará a cargo de implementar y validar los siguientes endpoints (GET, PATCH, DELETE)
Obtener un suite de prueba específico 
Actualizar un suite de prueba
Eliminar un suite de prueba
Gualberto Choque Choque
Asignado al módulo “Project” estará encargado de implementar y validar los siguientes endpoints (DELETE,GET):
Eliminar un proyecto por code
Obtener un proyecto por code
Herramientas
Postman 11.55.5
Git
Git Hub
Jira
Python 3.13.4
Pycharm 1.3.1


Recursos
- QA LEAD Gualberto Choque Choque
- QA Andres Adrian Estrada Uzeda
- QA David Gregori Rodriguez Calle
- QA Sol Abril Marquez Diaz
- QA Diego Armando Lomar Jain
