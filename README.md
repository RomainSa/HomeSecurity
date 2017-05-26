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
