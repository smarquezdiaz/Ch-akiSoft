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

**¿Por qué sería importante testearlo?**

Escogimos Qase porque nosotros al ser QA requerimos de esta aplicación como herramienta cotidiana y por tanto es requerida su funcionalidad con la menor cantidad de errores
Testear Qase es una prioridad absoluta porque la calidad de un producto de software es un reflejo directo de la calidad de las herramientas utilizadas para validarlo. Si la propia herramienta de QA falla, el proceso de aseguramiento de la calidad queda en entredicho. Es una responsabilidad crucial que la herramienta que usamos para garantizar la calidad en otros productos, sea de la más alta calidad posible.

La primera y principal razón es que los usuarios de Qase (equipos de QA y desarrolladores) dependen de la herramienta para gestionar sus procesos de prueba. Si la plataforma tiene errores, se vuelve poco confiable. Un error en la herramienta de gestión de pruebas podría, por ejemplo, perder datos de casos de prueba, borrar resultados de ejecución o fallar al generar informes. Esto podría llevar a que los equipos pierdan la confianza en Qase y busquen una alternativa.

2. Funcionalidades
Como equipo, determinamos escoger estas funcionalidades debido a la cantidad  de  métodos HTTP que ofrecen  de la API de Qase

#### **Attachments**
* Permite ver los archivos existentes, subir archivos (como imágenes o documentos), buscar un archivo en específico y eliminar un archivo en específico.

1.  **Obtener todos los archivos adjuntos**
    Permite listar una determinada cantidad de archivos y también omitir cierta cantidad de archivos con los siguientes parámetros:
    * `limit`
    * `offset`
    
2.  **Subir archivo adjunto**
    Permite subir un archivo que pese menos de 30MB y subir 20 archivos en conjunto a un proyecto.
    * `Code`
    * `File`
    
3.  **Obtener un archivo adjunto por Hash**
    Permite obtener un archivo en específico de un proyecto utilizando el Hash.
    * `Hash`
    
4.  **Eliminar un archivo adjunto mediante Hash**
    Permite eliminar un archivo en específico de un proyecto utilizando el Hash.
    * `Hash`

<br>

#### **Cases**
* Gestiona los casos de prueba individuales, incluyendo su creación, edición, recuperación y eliminación. Cada caso puede incluir pasos, resultados esperados y otros detalles clave.

1.  **Crear caso de prueba**
    Permite definir un nuevo caso de prueba, especificando:
    * Título y descripción
    * Pasos a seguir
    * Prioridad (baja, media, alta)
    * Severidad (baja, media, alta)
    * Tipo
    * Estado
    * Estado de automatización
    
2.  **Obtener un caso de prueba en específico**
    Recupera los detalles completos de un caso de prueba existente mediante su identificador único, mostrando todos los atributos, pasos y metadatos asociados.
    
3.  **Obtener todos los casos de prueba**
    Muestra un listado paginado de todos los casos de prueba de un proyecto, con filtros opcionales por:
    * Título y descripción
    * Pasos a seguir
    * Prioridad (baja, media, alta)
    * Severidad (baja, media, alta)
    * Tipo
    * Estado
    * Estado de automatización
    
4.  **Actualizar un caso de prueba**
    Modifica las propiedades de un caso ya creado, como:
    * Título y descripción
    * Pasos a seguir
    * Prioridad (baja, media, alta)
    * Severidad (baja, media, alta)
    * Tipo
    * Estado
    * Estado de automatización
    
5.  **Eliminar un caso de prueba**
    Borra de manera permanente un caso de prueba, retirándolo de la lista de casos disponibles en el proyecto.

<br>

#### **Custom Fields**
* Campos personalizados que se pueden crear para adaptarse a las necesidades específicas de documentación o flujo de trabajo del equipo.

1.  **Crear campo personalizado**
    Permite definir un nuevo campo adicional para adaptar los formularios a necesidades específicas del equipo.
    
2.  **Obtener todos los campos personalizados**
    Muestra una lista con todos los campos personalizados existentes creados en la cuenta.
    
3.  **Actualizar campo personalizado**
    Modifica las propiedades de un campo ya creado, como:
    * Nombre,
    * Tipo de dato o entidad asociada.
    
4.  **Eliminar campo personalizado**
    Borra un campo personalizado, eliminándolo de la lista de campos disponibles.
    
5.  **Asignar campo a una entidad específica**
    Especifica en qué módulo se utilizará el campo:
    * `Case`
    * `Run`
    * `Defect`
    
6.  **Definir tipo de dato del campo**
    Establece el formato del campo:
    * `number`
    * `string`
    * `text`
    * `selectbox`
    * `checkbox`
    * `radio`
    * `multiselect`
    * `url`
    * `user`
    * `datetime`

<br>

#### **Projects**
* El módulo Projects permite a los equipos de pruebas crear, visualizar, administrar y colaborar en diferentes proyectos de testing. Cada proyecto agrupa casos de prueba, suites, defectos, milestones y usuarios asignados. Es el punto de entrada para gestionar todos los artefactos de prueba de forma organizada y centralizada.

1.  **Create new project**
    Inicia el proceso de creación de un nuevo proyecto, especificando:
    * Nombre del proyecto
    * Código
    * Descripción
    * Visibilidad.
    
2.  **Barra de búsqueda y filtros**
    Permite buscar proyectos por su nombre. Los filtros disponibles son:
    * `Search for projects`
    * `Status: Active`
    * `Add filter`: Permite aplicar filtros personalizados adicionales.
    
3.  **Settings**
    Permite la configuración del proyecto (editar nombre, código, permisos, etc.).
    
4.  **Remove**
    Permite eliminar o archivar el proyecto.

<br>

#### **Suites**
* Agrupa los casos de prueba en conjuntos organizados por funcionalidades, módulos o criterios definidos por el equipo, facilitando la ejecución estructurada y el seguimiento de resultados.

1.  **Obtener todos los conjuntos de pruebas**
    Este método permite recuperar todos los conjuntos de pruebas de un proyecto.
    * **Filtrando por los parámetros:** `search`, `limit`, `offset`.
    * Se debe enviar el campo `code` como parámetro en la URL.
    
2.  **Crear un nuevo conjunto de pruebas**
    Este método crea un nuevo conjunto de pruebas a través de la API, enviando las propiedades:
    * `title` (requerido)
    * `description`
    * `preconditions`
    * `parent_id`
    
3.  **Obtener un conjunto de pruebas específico**
    Este método permite recuperar un conjunto de pruebas específico.
    * **Filtrando por los parámetros:** `search`, `limit`, `offset`.
    * Se deben enviar los campos `code` e `id` como parámetros en la URL.
    
4.  **Eliminar conjunto de pruebas**
    Este método elimina por completo un conjunto de pruebas del repositorio, enviando el campo `id` como parámetro en la URL.
    
5.  **Actualizar el conjunto de pruebas**
    Este método actualiza un conjunto de pruebas a través de la API, enviando las propiedades:
    * `title` (requerido)
    * `description`
    * `preconditions`
    * `parent_id`

<br>

#### **Plans**
* Permite crear un nuevo plan en un proyecto específico.

1.  **Crear un nuevo plan**
    Este método permite crear un plan en el proyecto seleccionado y contiene los siguientes puntos:
    * `Code`
    * `Title`
    * `Description`
    * `Cases`

  
3. Estrategia

Se emplearán las siguientes técnicas y tipos de pruebas para la validación de la API:

* Exploratory Testing: Se empleará esta técnica para explorar y comprender el comportamiento general de la aplicación, identificando posibles áreas de interés o problemas no documentados.

* Smoke Testing: Consiste en verificar que la API responda correctamente a las solicitudes básicas (código 200), asegurando que los componentes principales funcionen antes de realizar pruebas más exhaustivas. @pytest.mark.smoke

* Functional positive: Se valida que cada endpoint cumpla con su propósito y entregue los resultados esperados, asegurando el correcto funcionamiento según los requerimientos. Se usará la etiqueta @pytest.mark.positive

* Regression Testing: Se ejecutan pruebas para confirmar que los cambios o actualizaciones realizadas no afecten ni deterioren las funcionalidades previamente implementadas. Se aplicarán a todos los test cases. Se usará la etiqueta @pytest.mark.regression

* Functional negative: Se valida que el sistema maneje los errores de manera adecuada y permita observar el mensaje de error. Se usará la etiqueta @pytest.mark.negative

* End-to-End: Se demostrarán los flujos de funciones que evalúan un sistema completo desde el principio hasta el final, tal como lo haría un usuario real. Su objetivo es simular un flujo de trabajo completo para verificar que todas las partes de la aplicación funcionan juntas correctamente y sin interrupciones. Se usará la etiqueta @pytest.mark.e2e_{nombre_feature}

4. Alcance y Limitaciones

El presente plan de pruebas está enfocado en la validación funcional de los módulos workspace y project de Qase, con sus submódulos (Attachments, Cases,Custom Fields, Projects, Suites, Plan) Cualquier funcionalidad que no se menciona en este documento no se testeara

### Funcionalidades a ser Probadas

El proyecto consta de 20 endpoints pertenecientes a los módulos: `Attachments`, `Cases`, `Custom Fields`, `Projects`, `Suites`, y `Plans`.

#### 1er Sprint

Para este primer Sprint se contemplarán 10 endpoints de los cuales:

* **Diego Armando Lomar Jain**
    * **Módulo**: `Workspace`
    * **Submódulo**: `Attachment`
    * **Endpoints**:
        * Obtener todos los archivos adjuntos (`GET ALL`)
        * Subir archivo adjunto (`POST`)

* **Gualberto Choque Choque**
    * **Módulo**: `Project`
    * **Endpoints**:
        * Obtener todos los proyectos (`GET ALL`)
        * Crear nuevo proyecto (`POST`)

* **David Gregori Rodriguez Calle**
    * **Módulo**: `Project`
    * **Submódulo**: `Cases`
    * **Endpoints**:
        * Obtener todos los casos de prueba de un proyecto (`GET ALL`)
        * Crear un nuevo caso de prueba (`POST`)

* **Andres Adrian Estrada Uzeda**
    * **Módulo**: `Workspace`
    * **Submódulo**: `Custom Fields`
    * **Endpoints**:
        * Crear nuevo campo personalizado (`POST`)
        * Obtener campo personalizado por ID (`GET`)

* **Sol Abril Marquez Diaz**
    * **Módulo**: `Suites`
    * **Endpoints**:
        * Obtener todos los `suite` de prueba (`GET`)
        * Crear un nuevo `suite` (`POST`)
     
| Módulo | smoke | negative | positive | regression |
| :--- | :--- | :--- | :--- | :--- |
| Project | 12 | 21 | 14 | 35 |
| Attachment | 2 | 19 | 4 | 23 |
| custom field | 8 | 18 | 11 | 29 |
| cases | 3 | 23 | 30 | 53 |
| suite | 3 | 31 | 3 | 37 |
| **total** | **28** | **112** | **123** | **177** |


### 2do Sprint

Para este segundo Sprint se contemplarán los siguientes *endpoints* y flujos de trabajo:

* **Diego Armando Lomar Jain**
    * **Módulo**: `Project`
    * **Submódulo**: `Plan`
    * **Endpoints**:
        * Crear un nuevo plan (`POST`)
    * **Módulo**: `Workspace`
    * **Submódulo**: `Attachment`
    * **Endpoints**:
        * Eliminar archivo adjunto en específico (`DELETE`)
    * **User Story**: `DL-US005: End-to-End – Flujo Attachment`

* **David Gregori Rodriguez Calle**
    * **Módulo**: `Project`
    * **Submódulo**: `Cases`
    * **Endpoints**:
        * Actualizar un caso de prueba existente (`PATCH`)
        * Eliminar un caso de prueba por su ID (`DELETE`)
    * **User Story**: `DR-US05: End-to-End – Flujo Caso de prueba`

* **Andres Adrian Estrada Uzeda**
    * **Módulo**: `Workspace`
    * **Submódulo**: `Custom Fields`
    * **Endpoints**:
        * Crear nuevo campo personalizado (`DELETE`)
        * Actualizar campo personalizado por ID (`PATCH`)
    * **User Story**:
        * `AE-US03: Actualizar campo personalizado por ID`
        * `AE-US04: Eliminar campo personalizado por ID`
        * `AE-US05: End-to-End-Flujo completo de campo personalizado`

* **Sol Abril Marquez Diaz**
    * **Módulo**: `Suites`
    * **Endpoints**:
        * Actualizar un *suite* de prueba (`PATCH`)
        * Eliminar un *suite* de prueba (`DELETE`)
    * **User Story**: `SM-US005: End-to-End – Flujo Suite`

* **Gualberto Choque Choque**
    * **Módulo**: `Project`
    * **Endpoints**:
        * Eliminar un proyecto por `code` (`DELETE`)
        * Obtener un proyecto por `code` (`GET`)
    * **Observación**: Mejora del 1er Sprint (Refactorización de métodos del 1er sprint).
    * **User Story**: `GC-US005: End-to-End – Flujo Project`

| módulo | smoke | negative | positive | End to End | regresión |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Project | 11 | 26 | 11 | 1 | 37 |
| Attachment | 2 | 8 | 2 | 1 | 10 |
| Plan | 1 | 14 | 5 | 0 | 19 |
| custom field | 3 | 30 | 6 | 1 | 36 |
| cases | 5 | 33 | 21 | 1 | 54 |
| suite | 3 | 39 | 3 | 1 | 42 |
| **total** | **25** | **150** | **48** | **5** | **198** |

5. Herramientas
* Postman 11.55.5
* Git
* Git Hub
* Jira
* Python 3.13.4
* Pycharm 1.3.1

6. Tiempos Cronograma
   
   <img width="825" height="284" alt="image" src="https://github.com/user-attachments/assets/cbc0f9d8-8af8-4043-8b2d-cd0bc8d3d719" />

7. Recursos

* QA LEAD Gualberto Choque Choque
* QA Andres Adrian Estrada Uzeda
* QA David Gregori Rodriguez Calle
* QA Sol Abril Marquez Diaz
* QA Diego Armando Lomar Jain








