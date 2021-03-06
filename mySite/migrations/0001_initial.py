# Generated by Django 2.1.5 on 2019-01-09 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50, unique=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('datenaiss', models.DateField(db_column='dateNaiss')),
                ('lieunaiss', models.CharField(blank=True, db_column='lieuNaiss', max_length=50, null=True)),
                ('email', models.CharField(max_length=255)),
                ('mdp', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'etudiant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EtudiantEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etudiant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Etudiant')),
            ],
            options={
                'db_table': 'etudiant_evaluation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EtudiantFnPeriode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etudiant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Etudiant')),
            ],
            options={
                'db_table': 'etudiant_filiere_niveau_periode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'evaluation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.TextField()),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Filiere',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FiliereNiveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filiere', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Filiere')),
            ],
            options={
                'db_table': 'filiere_niveau',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('abr', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'Niveau',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datedebut', models.DateField(db_column='dateDebut')),
                ('datefin', models.DateField(db_column='dateFin')),
            ],
            options={
                'db_table': 'periode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('abr', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Semestre',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('Evaluation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fk_Session', to='mySite.Evaluation')),
            ],
            options={
                'db_table': 'session',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TypeEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=200)),
                ('abr', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'type_evaluation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ue',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UeFiliereNiveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('filiere_niveau', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.FiliereNiveau')),
                ('ue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Ue')),
            ],
            options={
                'db_table': 'ue_filiere_niveau',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='filiereniveau',
            name='niveau',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Niveau'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='periode',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Periode'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='semestre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Semestre'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='session',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fk_Evaluation', to='mySite.Session'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='type_evaluation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.TypeEvaluation'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='ue_fn',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.UeFiliereNiveau'),
        ),
        migrations.AddField(
            model_name='etudiantfnperiode',
            name='filiere_niveau',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.FiliereNiveau'),
        ),
        migrations.AddField(
            model_name='etudiantfnperiode',
            name='periode',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Periode'),
        ),
        migrations.AddField(
            model_name='etudiantevaluation',
            name='evaluation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mySite.Evaluation'),
        ),
    ]
