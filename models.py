# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    idcategoria = models.IntegerField(db_column='IdCategoria', primary_key=True)  # Field name made lowercase.
    detalle = models.TextField(db_column='Detalle')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categorias'


class Comentario(models.Model):
    idcomentario = models.IntegerField(db_column='IdComentario', primary_key=True)  # Field name made lowercase.
    idevento = models.IntegerField(db_column='IdEvento')  # Field name made lowercase.
    idlugar = models.IntegerField(db_column='IdLugar')  # Field name made lowercase.
    idfuncion = models.IntegerField(db_column='IdFuncion')  # Field name made lowercase.
    usuario = models.TextField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comentario'


class Departamentos(models.Model):
    iddepartamento = models.IntegerField(db_column='IdDepartamento', primary_key=True)  # Field name made lowercase.
    departamento = models.IntegerField(db_column='Departamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Edades(models.Model):
    idedad = models.IntegerField(db_column='IdEdad', primary_key=True)  # Field name made lowercase.
    edad = models.TextField(db_column='Edad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Edades'


class Eventos(models.Model):
    idevento = models.IntegerField(db_column='IdEvento', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    idcategoria = models.IntegerField(db_column='IdCategoria')  # Field name made lowercase.
    detalle = models.TextField(db_column='Detalle')  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal')  # Field name made lowercase.
    latitud = models.TextField(db_column='Latitud')  # Field name made lowercase. This field type is a guess.
    longitud = models.TextField(db_column='Longitud')  # Field name made lowercase. This field type is a guess.
    idedad = models.IntegerField(db_column='IdEdad', blank=True, null=True)  # Field name made lowercase.
    iddepartamento = models.IntegerField(db_column='IdDepartamento', blank=True, null=True)  # Field name made lowercase.
    contacto = models.TextField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    imagen = models.BinaryField(db_column='Imagen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eventos'


class Funiciones(models.Model):
    idfuncion = models.IntegerField(db_column='IdFuncion', primary_key=True)  # Field name made lowercase.
    idlugar = models.IntegerField(db_column='IdLugar')  # Field name made lowercase.
    funcion = models.IntegerField(db_column='Funcion')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    idedad = models.IntegerField(db_column='IdEdad', blank=True, null=True)  # Field name made lowercase.
    fotofuncion = models.BinaryField(db_column='FotoFuncion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funiciones'


class Lugares(models.Model):
    idlugar = models.IntegerField(db_column='IdLugar', primary_key=True)  # Field name made lowercase.
    idcategoria = models.IntegerField(db_column='IdCategoria', blank=True, null=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    iddepartamento = models.IntegerField(db_column='IdDepartamento')  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad', blank=True, null=True)  # Field name made lowercase.
    barrio = models.TextField(db_column='Barrio', blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    horario = models.TextField(db_column='Horario', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    tarjetas = models.TextField(db_column='Tarjetas', blank=True, null=True)  # Field name made lowercase.
    pagina = models.TextField(db_column='Pagina', blank=True, null=True)  # Field name made lowercase.
    tipocomida = models.TextField(db_column='TipoComida', blank=True, null=True)  # Field name made lowercase.
    gastopromedio = models.TextField(db_column='GastoPromedio', blank=True, null=True)  # Field name made lowercase.
    servicios = models.TextField(db_column='Servicios', blank=True, null=True)  # Field name made lowercase.
    latitud = models.TextField(db_column='Latitud', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitud = models.TextField(db_column='Longitud', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fotolugar = models.BinaryField(db_column='FotoLugar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugares'


class LugaresCines(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(db_column='Ciudad', max_length=10)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=150)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=150)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150)  # Field name made lowercase.
    pagina = models.CharField(db_column='Pagina', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugares_cines'


class LugaresLugar(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(db_column='Ciudad', max_length=10)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=150)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=150)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150)  # Field name made lowercase.
    pagina = models.CharField(db_column='Pagina', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugares_lugar'


class SalimosinicioCategorias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    categorias = models.CharField(db_column='Categorias', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salimosinicio_categorias'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HitcountBlacklistIp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ip = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'hitcount_blacklist_ip'


class HitcountBlacklistUserAgent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_agent = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'hitcount_blacklist_user_agent'


class HitcountHit(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    created = models.DateTimeField()
    ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    hitcount = models.ForeignKey('HitcountHitCount', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    session = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'hitcount_hit'


class HitcountHitCount(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    hits = models.PositiveIntegerField()
    modified = models.DateTimeField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    object_pk = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'hitcount_hit_count'
        unique_together = (('content_type', 'object_pk'),)


class UsuariosUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuarios_usuarios'
