from django.db import models

# Create your models here.


class Protein(models.Model):
    p_id = models.CharField(max_length=30)
    p_length = models.IntegerField()
    p_mass = models.IntegerField()
    p_accessions = models.CharField(max_length=300)
    p_sequence = models.TextField()
    p_sequence_score = models.TextField()
    p_sequence_type = models.TextField()

    def __str__(self):
        return self.p_id


class Protein2Drug(models.Model):
    protein_id = models.ManyToManyField(Protein)
    d_accession = models.CharField(max_length=30)
    d_name = models.CharField(max_length=300)

    def __str__(self):
        return self.d_accession
