Comparte Ride
=============

Group-bounded, invite-only, carpooling platform
# Hola!, encontré esta “regla de oro” para la cuestión de las vistas , por si te estas sumergiendo en django -REST y no sabes que tipo de vista usar:
+ViewSet: cuando usamos la mayoria de operaciones crud en un modelo

+Generics: cuando solo desee permitir algunas operaciones en un modelo

+ApiView :cuando desee personalizar completamente las operaciones de un modelo.

espero les sirva como una guia , mas no una regla

REST: estilo de arquitectura

Usar prurales

GET: list movies
POST: create a movie
PUT: updates movie
PATCH: partial updates a movie
DELETE: remove

No crecer a mas de dos niveles

Usar los parametros de las url
Para filtrar, ordenar

Usar alias

Fields:
Pagination:
Traer todos los elementos de un db
Informacion Adicional


HTTP: STATUS CODE

Cuando creas algo regresas eso que creaste es una convencion
Updates and creation should return a resource representation

Manejar los errores
Mensajes simples
Mensajes de validaciones por campos

Versiones
Subdomain
Stability
Consistency
Json First

snake_case

Authentication
Browser.Documentacion

Document your API

One thing you hate more than having

No puedes no usar SSL
Cache
Validar todo
Slug_name
crsf:
request limit:


Complementa tu api con SDK


### Request Response Renders parser
## Request
Renders: Se encargan de como esta saliendo el contenido
de nuestra api.
Usualmente se usa JSON

# Autenticaron

