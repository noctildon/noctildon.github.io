# hashtag is used for comments
# TAMU VPN is a must for anyone outside the campus. Set it up by following https://connect.tamu.edu/

#################################################################
### Linux basic commands
ssh NetID@terra.tamu.edu     # login to Terra
exit                         # disconnect
echo "Hello World"   # print
pwd                  # current directory
cd /home/username    # change directory
cd ..                # go to the parent directory
which python3        # check the path (used to check if the command exists or not)
python3 --version    # check the version
history              # list all commands you entered

ls      # list files
ls -l   # list files with details
ls -la  # list files with details and hidden files
ls | grep keyword   # list files filtered by a keyword

touch file.txt    # create an empty file
mkdir directory   # create an empty directory
rm file.txt       # remove a file **CAUTION** once removed, it cannot be recovered**
rm -r directory   # remove a directory (-r means recursive)
cp oldFile.txt newFile.txt      # copy a file
cp -r oldDirectory newDirectory # copy a directory
mv oldFile.txt newFile.txt      # move a file
mv oldDirectory newDirectory    # move a directory
cat file.txt           # read a file
nano file.txt          # edit a file (with nano editor)
chmod +x file.txt      # change the permission of a file (make it executable)
./script.sh            # run a script
./script.sh > log.txt  # run a script and save the output to a file
nohup ./script.sh > /dev/null 2>&1 & # run a script and detach

# copy file from local to remote
scp localFile.txt NetID@terra.tamu.edu:/scratch/user/NetID/remoteFile.txt
scp -r localFolder NetID@terra.tamu.edu:/scratch/user/NetID/remoteFolder

# copy file from remote to local
scp NetID@terra.tamu.edu:/scratch/user/NetID/remoteFile.txt localFile.txt
scp -r NetID@terra.tamu.edu:/scratch/user/NetID/remoteFolder localFolder


#################################################################
### Terra specific commands (https://hprc.tamu.edu/wiki/Terra)
cd $HOME                 # Home directory, limited space, where you usually save the settings
cd $SCRATCH              # navigate to SCRATCH folder because it has more space
showquota                # check the disk usage
sbatch job.slurm         # submit a job
squeue -u NetID          # check the status of a job
scancel jobID            # cancel a job
myproject                # check the SU balance
module spider Python/3   # search available modules by a keyword
module load intel/2020b  # load a module (or 'ml' for short)


### alias setting
nano ~/.bashrc               # edit the bashrc file
alias mp='myproject -l'      # add the shourtcut commands
alias sq='squeue -u NetID'   # alias SHORTCOMMAND='LONG COMMANDS'
source ~/.bashrc             # reload the bashrc file


### slurm job file. https://hprc.tamu.edu/wiki/Main_Page
#==================begin of job.slurm==================================#
#!/bin/bash

#SBATCH --time=1:30:00             # walltime 1hr 30min
#SBATCH --ntasks-per-node=28       # number of cores
#SBATCH --nodes=2                  # number of nodes
#SBATCH --mem-per-cpu=2000         # memory per CPU core
#SBATCH --job-name=%j              # job name (%j is the job id)
#SBATCH --output=%j.out            # output file name (anything that printed to terminal)
#SBATCH -e %j.err                  # error file name (if error occurs)
#SBATCH --account=1234567890       # account number

ml intel/2020b              # load the module
cd your_job_workspace       # navigate to the workspace
your_job_script.sh          # run the job script
python3 your_job_script.py  # could also be a python script
#===================end of job.slurm=================================#


#################################################################
### git (version control)
git init                  # initialize a git repository
git status                # check the status of the repository
git add .                 # add all files to the repository
git commit -m "message"   # commit the changes
git log                   # check the log (the commit history)
git checkout commitID     # switch to a commit

git branch                # check the branch
git branch branchName     # create a new branch
git checkout branchName   # switch to a branch


#################################################################
### Github
# Github is a website for hosting git repositories, and it's free
# It mainly serves two purposes: 1) share your code with others, 2) backup your code

git clone https://github.com/LazyVim/LazyVim  # download a github repository, no account needed

# register and create a new repository on the Github website, and set it private
git remote add origin  # add a remote repository
git push -u origin     # push the changes to the remote repository
git pull origin        # pull the changes from the remote repository


#################################################################
### unison: sync tool
# docs
# https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html
# https://github.com/bcpierce00/unison/wiki/Downloading-Unison

# quick install for mac and linux. It needs to be installed on both local and remote
# Mac: brew install unison
# Linux: sudo apt-get install unison

ln terra.prf ~/.unison # link to the home folder (may vary depending on the OS, see the manual for details)
unison terra           # sync the files between local and remote
# remember to add "ml unison" in .bashrc in Terra


#################################################################
# Other resources
# https://hprc.tamu.edu/training/primers_popup.html