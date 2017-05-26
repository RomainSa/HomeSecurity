# HomeSecurity

Les étapes pour activer la prise automatique de photos:
- [activer la caméra du raspberry](https://www.raspberrypi.org/documentation/usage/camera/README.md)
- télécharger DropBox UpLoader:
```bash
git clone https://github.com/andreafabrizi/Dropbox-Uploader
```
- le configurer:
```bash
./Dropbox-Uploader/dropbox_uploader.sh
```
- paramétrer un job CRON:
```bash
crontab -e
1 15 * * * /home/pi/camera/take-snapshot.sh
```
