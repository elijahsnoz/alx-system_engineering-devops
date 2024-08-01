<<<<<<< HEAD
0x0D-web_stack_debugging_0
=======
docker run -p 8080:80 -d -it holbertonschool/265-0
docker exec -it <container_id> /bin/bash
service apache2 start
service apache2 status  # Check if Apache is running
tail -f /var/log/apache2/error.log  # Check Apache error logs
netstat -tuln | grep :80  # Verify Apache is listening on port 80
service apache2 restart  # Restart Apache after fixing configuration
exit  # Exit the container shell
curl 0:8080  # Test accessing the page from host machine

>>>>>>> origin/main
