# Általános infó, előkészület
-  Git Bash letöltés: https://gitforwindows.org
-  Minden lenti parancs Git Bash terminálba írandó!
-  Git personal access token beállítása a gépeden:
```bash
cd ~
echo "https://<git user name>:<git access token>:github.com > .git-credentials
chmod 600 .git-credentials
git config --global credential.helper store
```

# Munkafolyamat
- Keress egy szimpatikus érettségit (https://www.oktatas.hu/kozneveles/erettsegi/feladatsorok)
- Csinálj a git repository-dban egy branchet, aminek add azt a nevet, hogy melyik éves érettségit csinálod
- Állj rá a branchre
- Hozz létre egy mappát ahova kódolni fogsz
- Old meg itt a programozási feladatot
- add és commit és push a branch-re az elkészült feladatot
- Csinálj egy Pull Request-et, és tegyél engem Review-ernek
- Ha ellenőríztem / review-ztam a kódot, fogok hozzá kommenteket írni --> ezek alapján javítsd a kódot
- Ha approve-oltam (le okéztam) a kódod, akkor a branch merge-elhető a fő / master branch-re 

# Parancsokhoz puska
### Bash parancsok
- mappa váltás (cd - change directory)
```bash
cd <cél mappa neve>
```
- mappa létrehozás (mkdir - make directory)
```bash
mkdir <létrehozandó mappa neve>
```
- aktuális mappa kilistázása (ls - list)
```bash
ls
```
- tetszőleges mappa kilistázása (ls - list)
```bash
ls <kilistázandó mappa neve>
```
- sok infós kilistázás (ls - list)
```bash
ls -ltrah <vagy nem írsz ide semmit / vagy egy kilistázandó mappa nevét>
```
- aktuális mappa elérési útvonalának lekérése (pwd - print working directory)
```bash
pwd
```
### git parancsok
- git repository clone-ozása
```bash
git clone <repository link>
```
- fájlok státuszának/állapotának lekérdezése (mi változott)
```bash
git status
```
- feltöltés (add, commit, push)
```bash
git add <feltöltendő file neve/elérési útvonala>
git commit -m "ide írd le hogy milyen módosítást csináltál"
git push
```
- remote repository szinkronizálása
```bash
git fetch --prune
```
- remote repository pull-olása
```bash 
git pull
```
- branch váltása
```bash
git checkout <branch neve amire át szeretnél állni>
```
- lokális változtatások elvetése
```bash
git stash
```
