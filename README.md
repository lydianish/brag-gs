# brag-gs
A Google Scholar API for BRAG

## Installation

```bash
pip install --user pipenv
cd brag-gs
pipenv install scholarly flask flask_restful
```

## Running the server locally

```bash
python server.py
```
The API will run locally on port `5002`.

## Example

A request for an author's information and publications:
``` 
GET http://localhost:5002/author?name=sophie+limou
```

Response:
```json
{
    "name": "Sophie Limou",
    "hIndex": 17,
    "citationCount": 1472,
    "citesPerYear": {
        "2009": 22,
        "2010": 46,
        "2011": 134,
        "2012": 110,
        "2013": 194,
        "2014": 150,
        "2015": 168,
        "2016": 184,
        "2017": 245,
        "2018": 203
    },
    "articles": [
        {
            "title": "APOL1 genetic variants in focal segmental glomerulosclerosis and HIV-associated nephropathy",
            "year": "",
            "citationCount": 414
        },
        {
            "title": "Genomewide Association Study of an AIDS-Nonprogression Cohort Emphasizes the Role Played by HLA Genes (ANRS Genomewide Association Study 02)",
            "year": "",
            "citationCount": 224
        },
        {
            "title": "CD39/adenosine pathway is involved in AIDS progression",
            "year": "",
            "citationCount": 114
        },
        {
            "title": "Genomewide association study of a rapid progression cohort identifies new susceptibility alleles for AIDS (ANRS Genomewide Association Study 03)",
            "year": "",
            "citationCount": 108
        },
        {
            "title": "APOL1 risk variants are strongly associated with HIV-associated nephropathy in black South Africans",
            "year": "",
            "citationCount": 86
        },
        {
            "title": "Multiple-cohort genetic association study reveals CXCR6 as a new chemokine receptor involved in long-term nonprogression to AIDS",
            "year": "",
            "citationCount": 72
        },
        {
            "title": "Genome-Wide Association Study Implicates PARD3B-Based AIDS Restriction",
            "year": "",
            "citationCount": 54
        },
        {
            "title": "APOL1 kidney risk alleles: population genetics and disease associations",
            "year": "",
            "citationCount": 52
        },
        {
            "title": "APOL1 kidney disease risk variants: an evolving landscape",
            "year": "",
            "citationCount": 48
        },
        {
            "title": "Genome-wide association study identifies single nucleotide polymorphism in DYRK1A associated with replication of HIV-1 in monocyte-derived macrophages",
            "year": "",
            "citationCount": 38
        },
        {
            "title": "DRAM triggers lysosomal membrane permeabilization and cell death in CD4+ T cells infected with HIV",
            "year": "",
            "citationCount": 33
        },
        {
            "title": "Genome-wide association scan in HIV-1-infected individuals identifying variants influencing disease course",
            "year": "",
            "citationCount": 31
        },
        {
            "title": "Screening low frequency SNPS from genome wide association study reveals a new risk allele for progression to AIDS",
            "year": "",
            "citationCount": 28
        },
        {
            "title": "APOL1-associated glomerular disease among African-American children: a collaboration of the Chronic Kidney Disease in Children (CKiD) and Nephrotic …",
            "year": "",
            "citationCount": 23
        },
        {
            "title": "APOL1 toxin, innate immunity, and kidney injury",
            "year": "",
            "citationCount": 21
        },
        {
            "title": "Multicohort genomewide association study reveals a new signal of protection against HIV-1 acquisition",
            "year": "",
            "citationCount": 21
        },
        {
            "title": "Identification of IL7RA risk alleles for rapid progression during HIV-1 infection: a comprehensive study in the GRIV cohort",
            "year": "",
            "citationCount": 20
        },
        {
            "title": "Sequencing rare and common APOL1 coding variants to determine kidney disease risk",
            "year": "",
            "citationCount": 15
        },
        {
            "title": "Immunogenetics: genome-wide association of non-progressive HIV and viral load control: HLA genes and beyond",
            "year": "",
            "citationCount": 15
        },
        {
            "title": "Exploration of associations between phospholipase A2 gene family polymorphisms and AIDS progression using the SNPlex™ method",
            "year": "",
            "citationCount": 13
        },
        {
            "title": "Genome-wide association of CKD progression: the chronic renal insufficiency cohort study",
            "year": "",
            "citationCount": 11
        },
        {
            "title": "Renal and cardiovascular morbidities associated with APOL1 status among African-American and non-African-American children with focal segmental glomerulosclerosis",
            "year": "",
            "citationCount": 8
        },
        {
            "title": "Variants in CXCR4 associate with juvenile idiopathic arthritis susceptibility",
            "year": "",
            "citationCount": 6
        },
        {
            "title": "APOL1-associated nephropathy: a key contributor to racial disparities in CKD",
            "year": "",
            "citationCount": 4
        },
        {
            "title": "APOL1 nephropathy risk variants do not associate with subclinical atherosclerosis or left ventricular mass in middle-aged black adults",
            "year": "",
            "citationCount": 4
        },
        {
            "title": "Lessons from CKD-Related Genetic Association Studies–Moving Forward",
            "year": "",
            "citationCount": 3
        },
        {
            "title": "Diving into the abyss of undiscovered kidney function–related factors",
            "year": "",
            "citationCount": 2
        },
        {
            "title": "APOL1 nephropathy risk variants and incident cardiovascular disease events in community-dwelling black adults",
            "year": "",
            "citationCount": 1
        },
        {
            "title": "Forecasting the future of cardiovascular disease in the United States: a policy statement from the American Heart Association.",
            "year": "",
            "citationCount": 1
        },
        {
            "title": "Renal cortical volume: High correlation with pre-and post-operative renal function in living kidney donors",
            "year": "",
            "citationCount": 1
        },
        {
            "title": "Ferret: a user-friendly Java tool to extract data from the 1000 Genomes Project",
            "year": "",
            "citationCount": 1
        },
        {
            "title": "23rd Nantes Actualités Transplantation:“Genomics and Immunogenetics of Kidney and Inflammatory Diseases–Lessons for Transplantation”",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "NPHS2 V260E Is a Frequent Cause of Steroid-Resistant Nephrotic Syndrome in Black South African Children",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "SNP-HLA REFERENCE CONSORTIUM: HLA AND SNP DATA SHARING FOR PROMOTING HLA-CENTRIC ANALYSES IN GENOMICS",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "A PRECISION MEDICINE APPLICATION: PERSONALIZED CONTEXTUALIZATION OF PATIENTS AFTER SOLID ORGAN TRANSPLANTATION",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "EPIGENOME-WIDE ASSOCIATION STUDY REVEALS IMMUNOGENETIC TARGETS OF DNA METHYLATION MODIFICATION BY HIV-1",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "HLA-DRB1* 09: 01 IS ASSOCIATED WITH A SEVERE ASTHMA OUTCOME IN THE CONSORTIUM ON ASTHMA AMONG AFRICAN-ANCESTRY POPULATIONS IN THE AMERICAS (CAAPA)",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "APPLICATION OF EASY-HLA TO 2,260 SOLID ORGAN TRANSPLANT DONOR-RECIPIENT PAIRS FROM 2 COHORTS: STATISTICALLY UPGRADED HLA TYPING FOR RESEARCH USE",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "EASYMATCH-R: THE VALIDATION OF A WEB APPLICATION FOR DONOR QUERY IN HAEMATOPOIETIC STEM CELL TRANSPLANTATION (HSCT)",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "Genetic screening of male patients with primary hypogammaglobulinemia can guide diagnosis and clinical management",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "P103 SNP-HLA reference consortium: HLA and SNP data sharing for promoting HLA centric analyses in genomics",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "SNP-HLA REFERENCE CONSORTIUM: HLA AND SNP DATA SHARING FOR PROMOTING HLA CENTRIC ANALYZES IN GENOMICS",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "THE KIDNEY TRANSPLANTATION APPLICATION (KITAPP): A VISUALIZATION AND CONTEXTUALIZATION TOOL IN A KIDNEY GRAFT PATIENT COHORT",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "FERRET: A USER-FRIENDLY TOOL TO EXTRACT DATA FROM THE 1000 GENOMES PROJECT",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "SNP-HLA REFERENCE CONSORTIUM: HLA AND SNP DATA SHARING FOR PROMOTING HLA CENTRIC ANALYSES IN GENOMICS",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "Multidimensional reduction of multicentric cohort heterogeneity: An alternative method to increase statistical power and robustness",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "nephrology digest",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "Integrative Biology of Renal Disease: The NEPTUNE Case Study",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "Genome-wide association study on HIV-1 susceptibility in Dutch high-risk seronegative individuals",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "Analyses' genome entier'de la cohorte griv de patients à profil extrême du sida",
            "year": "",
            "citationCount": 0
        },
        {
            "title": "SUPPLEMENT INTRODUCTION",
            "year": "",
            "citationCount": 0
        }
    ]
}
```