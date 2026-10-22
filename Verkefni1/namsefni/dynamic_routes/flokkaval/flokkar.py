from flask import Flask, render_template 
app = Flask(__name__)

# list [{dict}].
áfangar = [
    {
        'division': 'Vefþróun',
        'class': 'VEFÞ2VF5CU',
        'description':'Í áfanganum eru grunnatriði vefforritunar kynnt. Farið er í miðlara/biðlara uppbyggingu vefsíðna, samskipti þeirra og hlutverk hvers hluta. Nemendur vinna að smíði vefja með miðlaramáli. Lögð er áhersla á málfræði og endurnýtni á kóða í gerð vefja'
    },
    {
        'division': 'Vefþróun',
        'class': 'VEFÞ2VH5BU',
        'description':'Í áfanganum vinna nemendur að sveigjanlegri vefsíðuhönnun (e. Responsive Web Design) og skoða mismunandi aðferðir við uppsetningu (e. layout) snjallvefsíðna. Farið er í stílsetningu viðmiðunarmarka (e. breakpoints) í stílsíðu. Farið er í uppsetningu á samskiptaformi og töflu. Nemendur vinna með kvikun (e. animation) til að lífga upp á vefsíður og til að ná fram gagnvirkni í samskiptum vafra við notendur.'
    },
    {
        'division': 'Vefþróun',
        'class': 'VEFÞ1VG5AU',
        'description':'Í áfanganum er farið í grunnatriði vefsíðuhönnunar og megináhersla lögð á ívafsmál (e. HTML) og stílsíður (e. CSS). Hver þessara þátta er tekinn sérstaklega fyrir og sýnt hvernig samspil þeirra stuðlar að vandaðri uppsetningu og framsetningu vefsíðna. Skoðuð er þróunarsaga vefsins, hlutverk vafrans (e. Internet browser) og virkni hans.'
    },
    {
        'division': 'Tölvutækni',
        'class': 'KEST1TR05AU',
        'description':'Nemendur læra um mismunandi talnakerfi, lógískar aðgerðir og grunnatriði í Linux stýrikerfinu.'
    },
        {
        'division': 'Tölvutækni',
        'class': 'KEST2VJ05BU',
        'description':'Í áfanganum er megináhersla á vélbúnað og stýrikerfi. Nemendur setja saman tölvu, setja upp stýrikerfi, uppfæra BIOS, rekla og stýrikerfi. Farið er í hlutverk og samskipti mismunandi íhluta tölvunnar, s.s. örgjörva og minni, samskipti við viðskiptavini og þjónustuborð og förgun á tölvubúnaði. Fjallað er um tengingu og uppsetningu á jaðartækjum. Tengdar eru saman tvær eða fleiri tölvur þannig að þær geti haft samskipti sín á milli. Farið er í grunnatriði í rafmagnsfræði og hönnun á stýrirás. Nemendur hanna prótótýpu á brauðbretti og lóða rás á veroborð.'
    },
        {
        'division': 'Tölvutækni',
        'class': 'KEST2UN05CU',
        'description':'Í áfanganum er farið í undirstöðuatriði netkerfa. Farið er yfir hvernig netbúnaður hefur samskipti, vistföng og algengar netþjónustur. Einnig er farið í uppbyggingu heimanets og undirstöðuatriði í öryggisstillingum. Einnig er farið í prófanir og bilanagreiningu á netkerfisbúnaði.'
    },
]

@app.route('/')
def index():
    return render_template('flokkar.html', afangar=áfangar) 

# athugið að Jinja á ekki auðvelt með að höndla íslenska stafi í færibreytum!

@app.route('/afangaval/<division>')
def afangaval(division):
    grein = [val for val in áfangar if val["division"] == division]
    return render_template('afangaval.html', grein=grein)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  