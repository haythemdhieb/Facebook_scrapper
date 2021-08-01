use admin
db.createUser(
  {
     user: "root",
     pwd: "root",
     roles:["root"]
  }
);

use FbData
db.CreateUser(
   {
      user: "haythem",
      pwd: "1234",
      roles:[
         {
            role:"readwrite",
            db:"FbData"
         }
      ]

   }
);

