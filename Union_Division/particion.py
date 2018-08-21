cadena = "http://www.google.com".partition("www.")

protocolo , separador , dominio = cadena 

print("Protocolo: {0}\nDominio: {1}".format(protocolo , dominio))
