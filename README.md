# mailMorth
#Api Structure for intelijence (an email automation and management app)
#here goes the diagonal and logic list's of api's required to be created

what is clientKey ?
	create an clientKey for every client hoping to use the api,this clientKey would be a hashed base64 generated key based on the authKey provided by the client application and used to identify each client app request to access resources from the server.



		LIST OF API-CLASSES TO IMPLEMENT

		Name				|				Parameter

*: 		AuthClient 							(authKey)
	
		The api would be use to intiate an authKeyProcessor to validate that the client app is registered for this api and go through the list on the database of clients authKeys and once it matches, a session is stored down in the sessionManager folder in relation to other requests that may come from this particular client (User of the Clients device).
		This session is also used to track users of client apps and would be used to block any fradulent user activity or inproper handling of user's email resources by the client applications.

		This class returns
		-Nb: This is one of the procedures to make sure all clients using this wonderful api are authorised by us and are fit to start sending and receiving data.



1: 		start 								(clientAuth,email, password)
	
		The start api class would be collecting data using the post method, data include user email and email passwords, then an attempt to login into the client's email is made and if there is success



3: 		loadIntelijent 						(loggedAuthKey must be set)
	
		This page would be used to display all users account (All clients must make this view look like a folder so users can be aware that these are folders holding all their linked account)
