Cette application de bureau permet de suivre toutes les opérations comptables faites.
Cette une application très basique qui offre plusieurs fonctionnalités tel que:
  - La possibilité de voir son solde,
  - La possibilité de voir son solde prévisionnel,
  - La possibilité d'insérer une opération,
  - La possibilité de consulter l'historique des opérations,
  - De pouvoir filtrer cet historique pour retrouver certaines opérations en particulier,
  - De pouvoir modifier le type de certaines opérations.

Les types des opérations permettent de savoir si l'argent est en cours de transfert ("EN ATTENTE"), si l'opération a été refusée ("REFUSEE") ou bien si l'opération a été acceptée et que l'argent a bien été transféré ("ACCEPTEE")

Lorsque vous insérerez des opérations, si il s'agit d'une dépense, il vous suffira de mettre un - devant le montant afin d'indiquer à l'application qu'il s'agit d'une perte d'argent.
Pas besoin de mettre un + dans le cas d'un gain d'argent.

Dans l'onglet historique des opérations, pour pouvoir modifier une opération il faudra d'abord la sélectionner en cliquant simplement sur la ligne correspondante.

Cette application est connectée a une base de donnée MongoDB Atlas en ligne et gratuite.
Si vous souhaitez connecter cette application a une autre base de donnée MongoDB, il vous suffira de venir modifier les variables contenant les informations de connexion à la base de donnée situer à la fin du script.
