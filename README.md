# EC_MSUSERS

## Descripción

Microservicio capaz de administrar a los usuarios, dicho microservicio deberá de registrar los usuarios en una base de
datos de MongoDB Atlas, deberá de cumplir con los siguientes criterios:

- CA1: Los usuarios nuevos tendra la posibilidad de registrarse sin ningún
  requisito
- CA2: Como usuario registrado, tengo la posibilidad de consultar mis datos
  ingresando usuario y contraseña
- CA3: Al presentar mis credenciales correctas debo de recibir un Token único
  que me identifique como usuario autenticado

## Requerimientos

- [python 3.9 o mayor](https://www.python.org/)

## Instalación

### Local

#### virtualenv (Opcional)

instalar virtualenv

``` bash 
$ pip3 install virtualenv 
``` 

crear virtualenv

``` bash 
$ virtualenv venv 
``` 

activar virtualenv

- linux

``` bash 
$ ./venv/bin/activate
``` 

- windows

``` bash 
$ ./venv/Scripts/activate
``` 

#### Dependencias

instalacion de dependencias

``` bash 
$ pip3 install -r requirements.tx
``` 

#### Ejecutar

``` bash 
$ python3 main.py
``` 

### Docker

#### Descargar imagen

``` bash
$ docker pull ec_msusers:latest
```

#### Crear contenedor

``` bash
$ docker run -d -p --name container_ec_msusers ${puerto}:80 ec_msusers 
```

