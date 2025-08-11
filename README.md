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

PowerShell

```
scoop install allure
```

Puedes verificar la instalación ejecutando:

PowerShell

```
allure --version
```

4. Ejecución de pruebas y generación de reportes
Una vez que el plugin y la herramienta de Allure están instalados, puedes ejecutar tus pruebas y generar el reporte.

Ejecuta tus pruebas con Pytest, indicando la carpeta donde se guardarán los resultados. La bandera --alluredir es obligatoria.

Bash

```
pytest
```
Esto creará una carpeta llamada reports (puedes nombrarla como quieras) con los archivos de resultados.

Genera y visualiza el reporte HTML. Este comando tomará los archivos de la carpeta reports y creará un reporte visual que se abrirá automáticamente en tu navegador.

Bash

```
allure serve reports
```

## Test Plan

Nombre del plan: Test Plan – Qase
Versión: 1.0

Descripción del producto

Qase es una herramienta basada en la web para la gestión de pruebas de software. Está diseñada para ayudar a equipos de QA (Quality Assurance) y desarrollo a planificar, organizar, ejecutar y hacer seguimiento de casos de prueba de manera eficiente. Ofrece una interfaz intuitiva que permite mantener control sobre la cobertura de pruebas, identificar errores, y colaborar con los miembros del equipo en tiempo real. Además, proporciona herramientas para generar reportes, automatizar pruebas y mantener un historial centralizado del proceso de validación del producto.
Funcionalidades
Como equipo, determinamos escoger estas funcionalidades debido a la cantidad  de  métodos HTTP que ofrecen  de la API de Qase 

Attachments: Permite ver los archivos existentes, subir  archivos (como imágenes o documentos), buscar un archivo en especifico y eliminar un archivo en especifico.


Obtener todo los archivos adjuntos 
Permite listar una determinada cantidad de archivos y también omitir cierta cantidad de archivos con 
Limit
offset 
subir archivo adjunto
Permite subir un archivo que pese menos de 30MB y subir 20 archivos en conjunto a un proyecto. 
Code
File
Obtener un archivo adjunto por Hash
Permite obtener un archivo en específico de un proyecto utilizando el Hash 
Hash
Eliminar un archivo adjunto mediante Hash
	Permite eliminar un archivo en específico de un proyecto utilizando el Hash
Hash
Cases: Gestiona los casos de prueba individuales, incluyendo su creación, edición, recuperación y eliminación. Cada caso puede incluir pasos, resultados esperados y otros detalles clave.

Crear caso de prueba
Permite definir un nuevo caso de prueba, especificando:
Título y descripción
Pasos a seguir
Prioridad (baja, media, alta)
Severidad
Tipo
Estado
Estado de automatización
Obtener un caso de prueba en específico
Recupera los detalles completos de un caso de prueba existente mediante su identificador único, mostrando todos los atributos, pasos y metadatos asociados.
Obtener todos los casos de prueba
Muestra un listado paginado de todos los casos de prueba de un proyecto, con filtros opcionales por:
Título y descripción
Pasos a seguir
Prioridad (baja, media, alta)
Severidad
Tipo
Estado
Estado de automatización
Actualizar un caso de prueba
Modifica las propiedades de un caso ya creado, como:
Título o descripción
Pasos a seguir
Prioridad (baja, media, alta)
Severidad
Tipo
Estado
Estado de automatización
Eliminar un caso de prueba
Borra de manera permanente un caso de prueba, retirándolo de la lista de casos disponibles en el proyecto

Custom Fields
 Campos personalizados que se pueden crear para adaptarse a las necesidades específicas de documentación o flujo de trabajo del equipo.
Crear campo personalizado
Permite definir un nuevo campo adicional para adaptar los formularios a necesidades específicas del equipo.
Obtener todos los campos personalizados
Muestra una lista con todos los campos personalizados existentes creados en la cuenta.
Actualizar campo personalizado
Modifica las propiedades de un campo ya creado, 
Nombre,
 Tipo de dato o entidad asociada.
Eliminar campo personalizado
Borra un campo personalizado, 
eliminándolo de la lista de campos disponibles.
Asignar campo a una entidad específica
Especifica en qué módulo se utilizará el campo
Case 
Run
Defect 
Definir tipo de dato del campo
           Establece el formato del campo
 number;
string;
text;
selectbox;
checkbox;
radio;
multiselect;
url;
user;
datetime;                                                



Projects 
El módulo Projects permite a los equipos de pruebas crear, visualizar, administrar y colaborar en diferentes proyectos de testing. Cada proyecto agrupa casos de prueba, suites, defectos, milestones y usuarios asignados. Es el punto de entrada para gestionar todos los artefactos de prueba de forma organizada y centralizada.

1. Create new project
Inicia el proceso de creación de un nuevo proyecto.
nombre del proyecto
código
descripción
visibilidad.
2. Barra de búsqueda y filtros
                              Buscar por nombre del proyecto. Filtra los proyectos activos 
                              Permite aplicar más filtros personalizados 
Search for projects
Status: Active
Add filter
6. Settings: 
                             Configuración del proyecto (editar nombre, código, permisos, etc.).
7. Remove
      Eliminar o archivar el proyecto
Suites: Agrupa los casos de prueba en conjuntos organizados por funcionalidades, módulos o criterios definidos por el equipo, facilitando la ejecución estructurada y seguimiento de resultados.

Obtener todos los conjuntos de pruebas
Este método permite recuperar todos los conjuntos de pruebas almacenados en el proyecto seleccionado.
Filtrando por los parámetros:
search
limit
offset
		Y enviando como parámetro de la url, el campo code.

Crear un nuevo conjunto de pruebas
Este método se utiliza para crear un nuevo conjunto de pruebas a través de API.
Enviando las propiedades:
title(required)
description
preconditions
parent_id

Obtenga un conjunto de pruebas específico
Este método permite recuperar un conjunto de pruebas específico.
Filtrando por los parámetros:
search
limit
offset
		Y enviando como parámetro de la url, el campo code y id.

Eliminar conjunto de pruebas
Este método elimina por completo un conjunto de pruebas con casos de prueba del repositorio.
Enviando como parámetro de la url, el campo id.

Actualizar el conjunto de pruebas
Este método se utiliza para actualizar un conjunto de pruebas a través de API.
Enviando las propiedades:
title(required)
description
preconditions
parent_id

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
