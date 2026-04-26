import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def create_fuzzy_system():
    # Antecedents (Inputs)
    gaji = ctrl.Antecedent(np.arange(0, 15.1, 0.1), 'gaji') 
    relevansi = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'relevansi') 
    fleksibilitas = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'fleksibilitas') 
    reputasi = ctrl.Antecedent(np.arange(0, 10.1, 0.1), 'reputasi') # Variabel Baru

    # Consequent (Output)
    kelayakan = ctrl.Consequent(np.arange(0, 101, 1), 'kelayakan') 

    # Membership functions: Gaji (5 Tingkat dengan Gaussian & Trapezoidal)
    gaji['sangat_rendah'] = fuzz.trapmf(gaji.universe, [0, 0, 2, 3])
    gaji['rendah'] = fuzz.trapmf(gaji.universe, [2, 3, 4, 6])
    gaji['sedang'] = fuzz.gaussmf(gaji.universe, 7, 1.5)
    gaji['tinggi'] = fuzz.trapmf(gaji.universe, [8, 10, 12, 13])
    gaji['sangat_tinggi'] = fuzz.trapmf(gaji.universe, [11, 13, 15, 15])

    # Membership functions: Relevansi (3 Tingkat dengan Gaussian)
    relevansi['kurang'] = fuzz.gaussmf(relevansi.universe, 0, 2.5)
    relevansi['cukup'] = fuzz.gaussmf(relevansi.universe, 5, 2)
    relevansi['sangat'] = fuzz.gaussmf(relevansi.universe, 10, 2.5)

    # Membership functions: Fleksibilitas
    fleksibilitas['kaku'] = fuzz.trimf(fleksibilitas.universe, [0, 0, 4])
    fleksibilitas['sedang'] = fuzz.trimf(fleksibilitas.universe, [2, 5, 8])
    fleksibilitas['fleksibel'] = fuzz.trimf(fleksibilitas.universe, [6, 10, 10])

    # Membership functions: Reputasi
    reputasi['buruk'] = fuzz.trimf(reputasi.universe, [0, 0, 4])
    reputasi['standar'] = fuzz.trimf(reputasi.universe, [3, 5, 7])
    reputasi['unggul'] = fuzz.trimf(reputasi.universe, [6, 10, 10])

    # Membership functions: Kelayakan (5 Tingkat Output)
    kelayakan['sangat_tolak'] = fuzz.trapmf(kelayakan.universe, [0, 0, 15, 30])
    kelayakan['tolak'] = fuzz.trimf(kelayakan.universe, [20, 35, 50])
    kelayakan['pertimbangkan'] = fuzz.gaussmf(kelayakan.universe, 55, 10)
    kelayakan['terima'] = fuzz.trimf(kelayakan.universe, [60, 75, 90])
    kelayakan['sangat_layak'] = fuzz.trapmf(kelayakan.universe, [80, 90, 100, 100])

    # --- RULES BASE YANG LEBIH KOMPLEKS ---
    rules = []
    
    # 1. Rule Ekstrem Negatif (Sangat Tolak)
    rules.append(ctrl.Rule(reputasi['buruk'] & gaji['sangat_rendah'], kelayakan['sangat_tolak']))
    rules.append(ctrl.Rule(relevansi['kurang'] & gaji['sangat_rendah'], kelayakan['sangat_tolak']))
    rules.append(ctrl.Rule(reputasi['buruk'] & relevansi['kurang'], kelayakan['sangat_tolak']))

    # 2. Rule Tolak
    rules.append(ctrl.Rule(gaji['rendah'] & reputasi['buruk'], kelayakan['tolak']))
    rules.append(ctrl.Rule(gaji['rendah'] & relevansi['kurang'], kelayakan['tolak']))
    rules.append(ctrl.Rule(gaji['sedang'] & reputasi['buruk'] & fleksibilitas['kaku'], kelayakan['tolak']))
    rules.append(ctrl.Rule(gaji['sangat_rendah'] & reputasi['standar'], kelayakan['tolak']))

    # 3. Rule Pertimbangkan (Kondisi Moderat)
    rules.append(ctrl.Rule(gaji['sedang'] & relevansi['cukup'] & reputasi['standar'], kelayakan['pertimbangkan']))
    rules.append(ctrl.Rule(gaji['rendah'] & relevansi['sangat'] & reputasi['unggul'], kelayakan['pertimbangkan']))
    rules.append(ctrl.Rule(gaji['tinggi'] & relevansi['kurang'] & reputasi['standar'], kelayakan['pertimbangkan']))
    rules.append(ctrl.Rule(gaji['sangat_tinggi'] & reputasi['buruk'], kelayakan['pertimbangkan'])) # Gaji tinggi tapi rep buruk
    rules.append(ctrl.Rule(gaji['sedang'] & fleksibilitas['fleksibel'] & relevansi['kurang'], kelayakan['pertimbangkan']))

    # 4. Rule Terima
    rules.append(ctrl.Rule(gaji['tinggi'] & relevansi['cukup'] & reputasi['standar'], kelayakan['terima']))
    rules.append(ctrl.Rule(gaji['sedang'] & relevansi['sangat'] & reputasi['unggul'], kelayakan['terima']))
    rules.append(ctrl.Rule(gaji['sedang'] & relevansi['cukup'] & fleksibilitas['fleksibel'] & reputasi['unggul'], kelayakan['terima']))
    rules.append(ctrl.Rule(gaji['sangat_tinggi'] & relevansi['cukup'] & reputasi['standar'], kelayakan['terima']))

    # 5. Rule Ekstrem Positif (Sangat Layak)
    rules.append(ctrl.Rule(gaji['sangat_tinggi'] & relevansi['sangat'] & reputasi['unggul'], kelayakan['sangat_layak']))
    rules.append(ctrl.Rule(gaji['tinggi'] & relevansi['sangat'] & reputasi['unggul'] & fleksibilitas['fleksibel'], kelayakan['sangat_layak']))
    rules.append(ctrl.Rule(gaji['sangat_tinggi'] & relevansi['sangat'] & (fleksibilitas['sedang'] | fleksibilitas['fleksibel']), kelayakan['sangat_layak']))

    # Control system
    kelayakan_ctrl = ctrl.ControlSystem(rules)
    kelayakan_sim = ctrl.ControlSystemSimulation(kelayakan_ctrl)
    
    return kelayakan_sim

def evaluate_offer(val_gaji, val_relevansi, val_fleksibilitas, val_reputasi):
    sim = create_fuzzy_system()
    sim.input['gaji'] = val_gaji
    sim.input['relevansi'] = val_relevansi
    sim.input['fleksibilitas'] = val_fleksibilitas
    sim.input['reputasi'] = val_reputasi
    
    try:
        sim.compute()
        score = sim.output['kelayakan']
        
        # Determine string representation dynamically
        if score < 25:
            status = "Sangat Tolak"
        elif score < 45:
            status = "Tolak"
        elif score < 65:
            status = "Pertimbangkan"
        elif score < 85:
            status = "Terima"
        else:
            status = "Sangat Layak"
            
        return {
            "score": round(score, 2),
            "status": status
        }
    except Exception as e:
        print("Error during compute:", e)
        return {"score": 0, "status": "Error"}
