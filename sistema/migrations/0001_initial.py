# Generated by Django 3.2.3 on 2021-05-25 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comissionado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('salario', models.FloatField(default=1000)),
                ('metodo_de_pagamento', models.CharField(choices=[('1', 'Cheque Em Maos'), ('2', 'Cheque no Correio'), ('3', 'Deposito em Conta')], default='1', max_length=25)),
                ('pagamento', models.FloatField(blank=True, default=0, null=True)),
                ('comissao', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sindicato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_sindicato', models.CharField(default='Sindicato 1', max_length=25)),
                ('taxa', models.FloatField(default=0)),
                ('valor_sindicato', models.FloatField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField()),
                ('valor', models.FloatField()),
                ('comissionado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.comissionado')),
            ],
        ),
        migrations.CreateModel(
            name='Horista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('salario', models.FloatField(default=1000)),
                ('metodo_de_pagamento', models.CharField(choices=[('1', 'Cheque Em Maos'), ('2', 'Cheque no Correio'), ('3', 'Deposito em Conta')], default='1', max_length=25)),
                ('pagamento', models.FloatField(blank=True, default=0, null=True)),
                ('valor_hora', models.FloatField()),
                ('sindicato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.sindicato')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comissionado',
            name='sindicato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.sindicato'),
        ),
        migrations.CreateModel(
            name='CartaoDePonto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_trabalhadas', models.FloatField()),
                ('dia', models.DateField()),
                ('horista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sistema.horista')),
            ],
        ),
        migrations.CreateModel(
            name='Assalariado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('salario', models.FloatField(default=1000)),
                ('metodo_de_pagamento', models.CharField(choices=[('1', 'Cheque Em Maos'), ('2', 'Cheque no Correio'), ('3', 'Deposito em Conta')], default='1', max_length=25)),
                ('pagamento', models.FloatField(blank=True, default=0, null=True)),
                ('dia_do_pagamento', models.DateField()),
                ('sindicato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.sindicato')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
