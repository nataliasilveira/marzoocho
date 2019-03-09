# Generated by Django 2.1.7 on 2019-03-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategoria', models.IntegerField(db_column='IdCategoria', primary_key=True, serialize=False)),
                ('detalle', models.TextField(db_column='Detalle')),
            ],
            options={
                'db_table': 'Categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idcomentario', models.IntegerField(db_column='IdComentario', primary_key=True, serialize=False)),
                ('idevento', models.IntegerField(db_column='IdEvento')),
                ('idlugar', models.IntegerField(db_column='IdLugar')),
                ('idfuncion', models.IntegerField(db_column='IdFuncion')),
                ('usuario', models.TextField(blank=True, db_column='Usuario', null=True)),
                ('comentario', models.TextField(blank=True, db_column='Comentario', null=True)),
            ],
            options={
                'db_table': 'Comentario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('iddepartamento', models.IntegerField(db_column='IdDepartamento', primary_key=True, serialize=False)),
                ('departamento', models.IntegerField(db_column='Departamento')),
            ],
            options={
                'db_table': 'Departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Edades',
            fields=[
                ('idedad', models.IntegerField(db_column='IdEdad', primary_key=True, serialize=False)),
                ('edad', models.TextField(db_column='Edad')),
            ],
            options={
                'db_table': 'Edades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('idevento', models.IntegerField(db_column='IdEvento', primary_key=True, serialize=False)),
                ('nombre', models.TextField(db_column='Nombre')),
                ('idcategoria', models.IntegerField(db_column='IdCategoria')),
                ('detalle', models.TextField(db_column='Detalle')),
                ('fechainicio', models.DateField(db_column='FechaInicio')),
                ('fechafinal', models.DateField(db_column='FechaFinal')),
                ('latitud', models.TextField(db_column='Latitud')),
                ('longitud', models.TextField(db_column='Longitud')),
                ('idedad', models.IntegerField(blank=True, db_column='IdEdad', null=True)),
                ('iddepartamento', models.IntegerField(blank=True, db_column='IdDepartamento', null=True)),
                ('contacto', models.TextField(blank=True, db_column='Contacto', null=True)),
                ('ciudad', models.TextField(blank=True, db_column='Ciudad', null=True)),
                ('imagen', models.BinaryField(blank=True, db_column='Imagen', null=True)),
            ],
            options={
                'db_table': 'Eventos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funiciones',
            fields=[
                ('idfuncion', models.IntegerField(db_column='IdFuncion', primary_key=True, serialize=False)),
                ('idlugar', models.IntegerField(db_column='IdLugar')),
                ('funcion', models.IntegerField(db_column='Funcion')),
                ('fecha', models.DateField(blank=True, db_column='Fecha', null=True)),
                ('hora', models.TimeField(blank=True, db_column='Hora', null=True)),
                ('idedad', models.IntegerField(blank=True, db_column='IdEdad', null=True)),
                ('fotofuncion', models.BinaryField(blank=True, db_column='FotoFuncion', null=True)),
            ],
            options={
                'db_table': 'Funiciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HitcountBlacklistIp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'hitcount_blacklist_ip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HitcountBlacklistUserAgent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_agent', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'hitcount_blacklist_user_agent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HitcountHit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('ip', models.CharField(max_length=40)),
                ('user_agent', models.CharField(max_length=255)),
                ('session', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'hitcount_hit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HitcountHitCount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hits', models.PositiveIntegerField()),
                ('modified', models.DateTimeField()),
                ('object_pk', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'hitcount_hit_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('idlugar', models.IntegerField(db_column='IdLugar', primary_key=True, serialize=False)),
                ('idcategoria', models.IntegerField(blank=True, db_column='IdCategoria', null=True)),
                ('nombre', models.TextField(db_column='Nombre')),
                ('iddepartamento', models.IntegerField(db_column='IdDepartamento')),
                ('ciudad', models.TextField(blank=True, db_column='Ciudad', null=True)),
                ('barrio', models.TextField(blank=True, db_column='Barrio', null=True)),
                ('direccion', models.TextField(blank=True, db_column='Direccion', null=True)),
                ('horario', models.TextField(blank=True, db_column='Horario', null=True)),
                ('telefono', models.TextField(blank=True, db_column='Telefono', null=True)),
                ('tarjetas', models.TextField(blank=True, db_column='Tarjetas', null=True)),
                ('pagina', models.TextField(blank=True, db_column='Pagina', null=True)),
                ('tipocomida', models.TextField(blank=True, db_column='TipoComida', null=True)),
                ('gastopromedio', models.TextField(blank=True, db_column='GastoPromedio', null=True)),
                ('servicios', models.TextField(blank=True, db_column='Servicios', null=True)),
                ('latitud', models.TextField(blank=True, db_column='Latitud', null=True)),
                ('longitud', models.TextField(blank=True, db_column='Longitud', null=True)),
                ('fotolugar', models.BinaryField(blank=True, db_column='FotoLugar', null=True)),
            ],
            options={
                'db_table': 'Lugares',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LugaresCines',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(db_column='Ciudad', max_length=10)),
                ('direccion', models.CharField(db_column='Direccion', max_length=150)),
                ('fecha', models.CharField(db_column='Fecha', max_length=150)),
                ('telefono', models.CharField(db_column='Telefono', max_length=150)),
                ('pagina', models.CharField(db_column='Pagina', max_length=150)),
            ],
            options={
                'db_table': 'Lugares_cines',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LugaresLugar',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.CharField(db_column='Ciudad', max_length=10)),
                ('direccion', models.CharField(db_column='Direccion', max_length=150)),
                ('fecha', models.CharField(db_column='Fecha', max_length=150)),
                ('telefono', models.CharField(db_column='Telefono', max_length=150)),
                ('pagina', models.CharField(db_column='Pagina', max_length=150)),
            ],
            options={
                'db_table': 'Lugares_lugar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalimosinicioCategorias',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('categorias', models.CharField(db_column='Categorias', max_length=500)),
            ],
            options={
                'db_table': 'Salimosinicio_categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosUsuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'usuarios_usuarios',
                'managed': False,
            },
        ),
    ]
