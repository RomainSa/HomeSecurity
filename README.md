# HomeSecurity

Les étapes pour activer la prise automatique de photos:
- [activer la caméra du raspberry](https://www.raspberrypi.org/documentation/usage/camera/README.md)
- créer un dossier pour le projet:
```bash
mkdir camera && cd camera
```
- télécharger DropBox UpLoader:
```bash
git clone https://github.com/andreafabrizi/Dropbox-Uploader
```
- le configurer:
```bash
./Dropbox-Uploader/dropbox_uploader.sh
```
- télécharger ce projet:
```bash
git clone https://github.com/RomainSa/HomeSecurity.git
```
- paramétrer un job CRON:
```bash
crontab -e
1 0 * * * /home/pi/camera/HomeSecurity/snapshot.sh
```
- donner login et mot de passe et lancer le serveur web Flask
```bash
export FLASK_APP=home.py
export FLASK_LOGIN=???
export FLASK_PASSWORD=???
export FLASK_APP_URL=???
python -m flask run --host=0.0.0.0
```
