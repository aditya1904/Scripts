#!/bin/bash

mkdir LDAP && cd LDAP
touch final.ldif
c=newldap
echo "dn: ou=$c,dc=test,dc=com\nobjectClass: organizationalUnit\nou: $c" > group.ldif
ldapadd -x -D "cn=admin,dc=test,dc=com" -w root -f group.ldif
n=12001
i=0
while [ $i -lt $1 ]
do
	s=`expr $n + $i`
	u=`expr $i + 10000`
	echo "dn: cn=$n,ou=$c,dc=test,dc=com\nou: IT-Dept\nobjectClass: top\nobjectClass: inetOrgPerson\nobjectClass: posixAccount\ncn: $n\nsn: $s\nuid: $i\nuidNumber: $u\ngidNumber: 100\nhomeDirectory: /home\nuserPassword:root{crypt}$n\nmail: $n@coep.ac.in\nhomephone: $n" > $n.ldif
	cat $n.ldif >> final.ldif
	echo "" >> final.ldif
	n=`expr $n + 1`
	i=`expr $i + 1`
done

ldapadd -x -D "cn=admin,dc=test,dc=com" -w root -f final.ldif


