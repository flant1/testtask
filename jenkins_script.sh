dirname=$(date +%s)
mkdir $dirname
cd $dirname
git clone https://github.com/flant1/testtask.git
cd testtask
echo 'FROM python:3.10.5
RUN pip install git-python
COPY weblisten.py /
COPY .git/ /
EXPOSE 8080
CMD ["python3","weblisten.py"]' > Dockerfile
docker build -t $dirname .
prev=$(cat /var/lib/jenkins/workspace/item1/previous)
docker service rm $prev
rm -r /var/lib/jenkins/workspace/item1/$prev
docker tag $dirname 192.168.56.114:5001/$dirname
docker push 192.168.56.114:5001/$dirname
terraform -chdir=/var/lib/jenkins/workspace/item1 apply -var servicename="$dirname" -var imagename="192.168.56.114:5001/$dirname" -auto-approve
echo $dirname > /var/lib/jenkins/workspace/item1/previous
docker stop $(docker ps|grep $dirname|cut -d' ' -f1) -t 30 &
