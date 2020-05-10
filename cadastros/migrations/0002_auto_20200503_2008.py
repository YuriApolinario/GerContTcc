# Generated by Django 2.2.10 on 2020-05-03 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateField(max_length=8)),
                ('data_final', models.DateField(max_length=8)),
                ('registrado_em', models.DateField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('sexo', models.CharField(max_length=10, unique=True)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_servico', models.CharField(max_length=100)),
                ('valor', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='contratada',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='cidade',
        ),
        migrations.AddField(
            model_name='empresa',
            name='minha_empresa',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Contrante',
        ),
        migrations.DeleteModel(
            name='Contratada',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.User'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='contratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Empresa'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='propriedade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Propriedade'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='registrado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.User'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Servico'),
        ),
    ]