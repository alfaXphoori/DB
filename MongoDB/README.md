### MongoDB Atlas
## MongoDB
* Register
* Login
```bash
https://www.mongodb.com/cloud/atlas/register
```
#### Create Cluster
```bash
DEPLOYMENT -> Database -> Build Cluster -> M0 (Free) -> Create Deployment
```
* Name = Ce_cluster
* Provider = aws
#### Upgrade Cluster
```bash
DEPLOYMENT -> Database -> Ce_cluster -> Edit Congiguration -> M0 -> Edit Additional Config -> Choose it 
```
#### Setup Network Acccess
```bash
SECURITY -> Netowork Access -> Allow Accress form anywhere -> Confirm
```
#### ADD New Database User
```bash
SECURITY -> Database Access -> ADD NEW DATABASE USER -> Passwoed -> Password Authentication -> Built In Role -> Add User
```
* Built In Role = Read and write to any database
#### Create Collentions
```bash
DEPLOYMENT -> Database -> Ce_cluster -> Browse Collentions -> Create Database
```
* Database name = iotDB
* collection name = picoW
* Additional Preferenses = Clustered Index Collection
#### Insert Document
```bash
iotDB -> picoW -> INSERT DOCUMENT
```
* Insert json Document 
#### Connect MongoDB via Python
```bash
DEPLOYMENT -> Database -> Ce_cluster -> Connect -> Drivers 
```
* Driver = Python