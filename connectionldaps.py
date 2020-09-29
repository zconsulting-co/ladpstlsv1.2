from ldap3 import Server, Connection, Tls, SASL, GSSAPI, ALL
import ssl, sys

serv= sys.argv[1]
tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
server = Server(serv, use_ssl=True, tls=tls, get_info=ALL)
c = Connection(server, authentication=SASL, sasl_mechanism=GSSAPI)
c.bind()
print(c.extend.standard.who_am_i())
# c.unbind()