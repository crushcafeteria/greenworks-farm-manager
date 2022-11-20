@servers(['production' => 'root@lipasafe.com', 'localhost' => '127.0.0.1'])


@task('push_to_vc', ['on' => 'localhost'])
cd /var/www/python/greenworks/
git add .
git commit -m "Automatic deployment on $(date)"
git push origin main
echo "COMPLETE => Source code successfully pushed to Git!"
@endtask

@task('deploy_on_server', ['on'=>'production'])
    cd /mnt/www/greenworks/farm-manager
    git pull origin main
    source ../venv/bin/activate
    pip install -r requirements.txt
@endtask

@story('deploy')
push_to_vc
deploy_on_server
@endstory
