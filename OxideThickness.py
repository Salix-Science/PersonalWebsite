import math
import cmath
import numpy as np
from scipy import optimize
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
global ref_intensity
ref_intensity = None
calcd = 0
global result
result = 0
def n_SiO2(wavelength_nm):
    wl = wavelength_nm / 1000
    n = math.sqrt(1 + (0.6961663 * wl**2) / (wl**2 - 0.0046791) 
                    + (0.4079426 * wl**2) / (wl**2 - 0.0135121) 
                    + (0.8974794 * wl**2) / (wl**2 - 97.9340025))
    return n
def n_Si(wavelength_nm):
    # 400 points, 1 nm steps, 400–799 nm
    # n and k values linearly interpolated from Palik/Green tabulated data at 10 nm nodes
    si_wl = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409,
             410, 411, 412, 413, 414, 415, 416, 417, 418, 419,
             420, 421, 422, 423, 424, 425, 426, 427, 428, 429,
             430, 431, 432, 433, 434, 435, 436, 437, 438, 439,
             440, 441, 442, 443, 444, 445, 446, 447, 448, 449,
             450, 451, 452, 453, 454, 455, 456, 457, 458, 459,
             460, 461, 462, 463, 464, 465, 466, 467, 468, 469,
             470, 471, 472, 473, 474, 475, 476, 477, 478, 479,
             480, 481, 482, 483, 484, 485, 486, 487, 488, 489,
             490, 491, 492, 493, 494, 495, 496, 497, 498, 499,
             500, 501, 502, 503, 504, 505, 506, 507, 508, 509,
             510, 511, 512, 513, 514, 515, 516, 517, 518, 519,
             520, 521, 522, 523, 524, 525, 526, 527, 528, 529,
             530, 531, 532, 533, 534, 535, 536, 537, 538, 539,
             540, 541, 542, 543, 544, 545, 546, 547, 548, 549,
             550, 551, 552, 553, 554, 555, 556, 557, 558, 559,
             560, 561, 562, 563, 564, 565, 566, 567, 568, 569,
             570, 571, 572, 573, 574, 575, 576, 577, 578, 579,
             580, 581, 582, 583, 584, 585, 586, 587, 588, 589,
             590, 591, 592, 593, 594, 595, 596, 597, 598, 599,
             600, 601, 602, 603, 604, 605, 606, 607, 608, 609,
             610, 611, 612, 613, 614, 615, 616, 617, 618, 619,
             620, 621, 622, 623, 624, 625, 626, 627, 628, 629,
             630, 631, 632, 633, 634, 635, 636, 637, 638, 639,
             640, 641, 642, 643, 644, 645, 646, 647, 648, 649,
             650, 651, 652, 653, 654, 655, 656, 657, 658, 659,
             660, 661, 662, 663, 664, 665, 666, 667, 668, 669,
             670, 671, 672, 673, 674, 675, 676, 677, 678, 679,
             680, 681, 682, 683, 684, 685, 686, 687, 688, 689,
             690, 691, 692, 693, 694, 695, 696, 697, 698, 699,
             700, 701, 702, 703, 704, 705, 706, 707, 708, 709,
             710, 711, 712, 713, 714, 715, 716, 717, 718, 719,
             720, 721, 722, 723, 724, 725, 726, 727, 728, 729,
             730, 731, 732, 733, 734, 735, 736, 737, 738, 739,
             740, 741, 742, 743, 744, 745, 746, 747, 748, 749,
             750, 751, 752, 753, 754, 755, 756, 757, 758, 759,
             760, 761, 762, 763, 764, 765, 766, 767, 768, 769,
             770, 771, 772, 773, 774, 775, 776, 777, 778, 779,
             780, 781, 782, 783, 784, 785, 786, 787, 788, 789,
             790, 791, 792, 793, 794, 795, 796, 797, 798, 799]
    si_n  = [5.5700, 5.5484, 5.5268, 5.5052, 5.4836, 5.4620, 5.4404, 5.4188, 5.3972, 5.3756,
             5.3540, 5.3346, 5.3152, 5.2958, 5.2764, 5.2570, 5.2376, 5.2182, 5.1988, 5.1794,
             5.1600, 5.1425, 5.1250, 5.1075, 5.0900, 5.0725, 5.0550, 5.0375, 5.0200, 5.0025,
             4.9850, 4.9693, 4.9536, 4.9379, 4.9222, 4.9065, 4.8908, 4.8751, 4.8594, 4.8437,
             4.8280, 4.8138, 4.7996, 4.7854, 4.7712, 4.7570, 4.7428, 4.7286, 4.7144, 4.7002,
             4.6860, 4.6732, 4.6604, 4.6476, 4.6348, 4.6220, 4.6092, 4.5964, 4.5836, 4.5708,
             4.5580, 4.5466, 4.5352, 4.5238, 4.5124, 4.5010, 4.4896, 4.4782, 4.4668, 4.4554,
             4.4440, 4.4337, 4.4234, 4.4131, 4.4028, 4.3925, 4.3822, 4.3719, 4.3616, 4.3513,
             4.3410, 4.3318, 4.3226, 4.3134, 4.3042, 4.2950, 4.2858, 4.2766, 4.2674, 4.2582,
             4.2490, 4.2407, 4.2324, 4.2241, 4.2158, 4.2075, 4.1992, 4.1909, 4.1826, 4.1743,
             4.1660, 4.1586, 4.1512, 4.1438, 4.1364, 4.1290, 4.1216, 4.1142, 4.1068, 4.0994,
             4.0920, 4.0853, 4.0786, 4.0719, 4.0652, 4.0585, 4.0518, 4.0451, 4.0384, 4.0317,
             4.0250, 4.0188, 4.0126, 4.0064, 4.0002, 3.9940, 3.9878, 3.9816, 3.9754, 3.9692,
             3.9630, 3.9574, 3.9518, 3.9462, 3.9406, 3.9350, 3.9294, 3.9238, 3.9182, 3.9126,
             3.9070, 3.9019, 3.8968, 3.8917, 3.8866, 3.8815, 3.8764, 3.8713, 3.8662, 3.8611,
             3.8560, 3.8513, 3.8466, 3.8419, 3.8372, 3.8325, 3.8278, 3.8231, 3.8184, 3.8137,
             3.8090, 3.8047, 3.8004, 3.7961, 3.7918, 3.7875, 3.7832, 3.7789, 3.7746, 3.7703,
             3.7660, 3.7620, 3.7580, 3.7540, 3.7500, 3.7460, 3.7420, 3.7380, 3.7340, 3.7300,
             3.7260, 3.7224, 3.7188, 3.7152, 3.7116, 3.7080, 3.7044, 3.7008, 3.6972, 3.6936,
             3.6900, 3.6866, 3.6832, 3.6798, 3.6764, 3.6730, 3.6696, 3.6662, 3.6628, 3.6594,
             3.6560, 3.6529, 3.6498, 3.6467, 3.6436, 3.6405, 3.6374, 3.6343, 3.6312, 3.6281,
             3.6250, 3.6221, 3.6192, 3.6163, 3.6134, 3.6105, 3.6076, 3.6047, 3.6018, 3.5989,
             3.5960, 3.5933, 3.5906, 3.5879, 3.5852, 3.5825, 3.5798, 3.5771, 3.5744, 3.5717,
             3.5690, 3.5665, 3.5640, 3.5615, 3.5590, 3.5565, 3.5540, 3.5515, 3.5490, 3.5465,
             3.5440, 3.5417, 3.5394, 3.5371, 3.5348, 3.5325, 3.5302, 3.5279, 3.5256, 3.5233,
             3.5210, 3.5189, 3.5168, 3.5147, 3.5126, 3.5105, 3.5084, 3.5063, 3.5042, 3.5021,
             3.5000, 3.4980, 3.4960, 3.4940, 3.4920, 3.4900, 3.4880, 3.4860, 3.4840, 3.4820,
             3.4800, 3.4782, 3.4764, 3.4746, 3.4728, 3.4710, 3.4692, 3.4674, 3.4656, 3.4638,
             3.4620, 3.4603, 3.4586, 3.4569, 3.4552, 3.4535, 3.4518, 3.4501, 3.4484, 3.4467,
             3.4450, 3.4434, 3.4418, 3.4402, 3.4386, 3.4370, 3.4354, 3.4338, 3.4322, 3.4306,
             3.4290, 3.4275, 3.4260, 3.4245, 3.4230, 3.4215, 3.4200, 3.4185, 3.4170, 3.4155,
             3.4140, 3.4127, 3.4114, 3.4101, 3.4088, 3.4075, 3.4062, 3.4049, 3.4036, 3.4023,
             3.4010, 3.3997, 3.3984, 3.3971, 3.3958, 3.3945, 3.3932, 3.3919, 3.3906, 3.3893,
             3.3880, 3.3868, 3.3856, 3.3844, 3.3832, 3.3820, 3.3808, 3.3796, 3.3784, 3.3772,
             3.3760, 3.3749, 3.3738, 3.3727, 3.3716, 3.3705, 3.3694, 3.3683, 3.3672, 3.3661,
             3.3650, 3.3639, 3.3628, 3.3617, 3.3606, 3.3595, 3.3584, 3.3573, 3.3562, 3.3551,
             3.3540, 3.3530, 3.3520, 3.3510, 3.3500, 3.3490, 3.3480, 3.3470, 3.3460, 3.3450,
             3.3440, 3.3431, 3.3422, 3.3413, 3.3404, 3.3395, 3.3386, 3.3377, 3.3368, 3.3359,
             3.3350, 3.3341, 3.3332, 3.3323, 3.3314, 3.3305, 3.3296, 3.3287, 3.3278, 3.3269,
             3.3260, 3.3252, 3.3244, 3.3236, 3.3228, 3.3220, 3.3212, 3.3204, 3.3196, 3.3188]
    si_k  = [0.3870, 0.3829, 0.3788, 0.3747, 0.3706, 0.3665, 0.3624, 0.3583, 0.3542, 0.3501,
             0.3460, 0.3417, 0.3374, 0.3331, 0.3288, 0.3245, 0.3202, 0.3159, 0.3116, 0.3073,
             0.3030, 0.2987, 0.2944, 0.2901, 0.2858, 0.2815, 0.2772, 0.2729, 0.2686, 0.2643,
             0.2600, 0.2562, 0.2524, 0.2486, 0.2448, 0.2410, 0.2372, 0.2334, 0.2296, 0.2258,
             0.2220, 0.2189, 0.2158, 0.2127, 0.2096, 0.2065, 0.2034, 0.2003, 0.1972, 0.1941,
             0.1910, 0.1882, 0.1854, 0.1826, 0.1798, 0.1770, 0.1742, 0.1714, 0.1686, 0.1658,
             0.1630, 0.1607, 0.1584, 0.1561, 0.1538, 0.1515, 0.1492, 0.1469, 0.1446, 0.1423,
             0.1400, 0.1379, 0.1358, 0.1337, 0.1316, 0.1295, 0.1274, 0.1253, 0.1232, 0.1211,
             0.1190, 0.1172, 0.1154, 0.1136, 0.1118, 0.1100, 0.1082, 0.1064, 0.1046, 0.1028,
             0.1010, 0.0995, 0.0980, 0.0965, 0.0950, 0.0935, 0.0920, 0.0905, 0.0890, 0.0875,
             0.0860, 0.0847, 0.0834, 0.0821, 0.0808, 0.0795, 0.0782, 0.0769, 0.0756, 0.0743,
             0.0730, 0.0719, 0.0708, 0.0697, 0.0686, 0.0675, 0.0664, 0.0653, 0.0642, 0.0631,
             0.0620, 0.0610, 0.0600, 0.0590, 0.0580, 0.0570, 0.0560, 0.0550, 0.0540, 0.0530,
             0.0520, 0.0512, 0.0504, 0.0496, 0.0488, 0.0480, 0.0472, 0.0464, 0.0456, 0.0448,
             0.0440, 0.0433, 0.0426, 0.0419, 0.0412, 0.0405, 0.0398, 0.0391, 0.0384, 0.0377,
             0.0370, 0.0364, 0.0358, 0.0352, 0.0346, 0.0340, 0.0334, 0.0328, 0.0322, 0.0316,
             0.0310, 0.0305, 0.0300, 0.0295, 0.0290, 0.0285, 0.0280, 0.0275, 0.0270, 0.0265,
             0.0260, 0.0256, 0.0252, 0.0248, 0.0244, 0.0240, 0.0236, 0.0232, 0.0228, 0.0224,
             0.0220, 0.0216, 0.0212, 0.0208, 0.0204, 0.0200, 0.0196, 0.0192, 0.0188, 0.0184,
             0.0180, 0.0177, 0.0174, 0.0171, 0.0168, 0.0165, 0.0162, 0.0159, 0.0156, 0.0153,
             0.0150, 0.0148, 0.0146, 0.0144, 0.0142, 0.0140, 0.0138, 0.0136, 0.0134, 0.0132,
             0.0130, 0.0128, 0.0126, 0.0124, 0.0122, 0.0120, 0.0118, 0.0116, 0.0114, 0.0112,
             0.0110, 0.0108, 0.0106, 0.0104, 0.0102, 0.0100, 0.0098, 0.0096, 0.0094, 0.0092,
             0.0090, 0.0088, 0.0086, 0.0084, 0.0082, 0.0080, 0.0078, 0.0076, 0.0074, 0.0072,
             0.0070, 0.0069, 0.0068, 0.0067, 0.0066, 0.0065, 0.0064, 0.0063, 0.0062, 0.0061,
             0.0060, 0.0059, 0.0058, 0.0057, 0.0056, 0.0055, 0.0054, 0.0053, 0.0052, 0.0051,
             0.0050, 0.0049, 0.0048, 0.0047, 0.0046, 0.0045, 0.0044, 0.0043, 0.0042, 0.0041,
             0.0040, 0.0040, 0.0040, 0.0040, 0.0040, 0.0040, 0.0040, 0.0040, 0.0040, 0.0040,
             0.0040, 0.0039, 0.0038, 0.0037, 0.0036, 0.0035, 0.0034, 0.0033, 0.0032, 0.0031,
             0.0030, 0.0030, 0.0030, 0.0030, 0.0030, 0.0030, 0.0030, 0.0030, 0.0030, 0.0030,
             0.0030, 0.0029, 0.0028, 0.0027, 0.0026, 0.0025, 0.0024, 0.0023, 0.0022, 0.0021,
             0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020,
             0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020,
             0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020, 0.0020,
             0.0020, 0.0019, 0.0018, 0.0017, 0.0016, 0.0015, 0.0014, 0.0013, 0.0012, 0.0011,
             0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010,
             0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010,
             0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010,
             0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010,
             0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010]
    n  = np.interp(wavelength_nm, si_wl, si_n)
    k  = np.interp(wavelength_nm, si_wl, si_k)
    return n + 1j * k

def fresnel_reflectance(wavelength_nm, thickness_nm):
    # returns R (0 to 1) for SiO2 on Si at normal incidence
    nSiO2 = n_SiO2(wavelength_nm)
    nSi = n_Si(wavelength_nm)
    r12 = ((1.0003 - nSiO2) / (1.0003 + nSiO2))
    r23 = ((nSiO2 - nSi) / (nSiO2 + nSi))
    delta = 2 * math.pi * nSiO2 * thickness_nm / wavelength_nm
    z = 2j * delta 
    R = abs( (r12 + r23 * cmath.exp(z)) / (1 + r12 * r23 * cmath.exp(z)) ) ** 2
    return R

#write program that returns best fit thickness of 2 numpy arrays
wavelengths = np.array([400,600,800])
R_measured = np.array([fresnel_reflectance(400, 120),fresnel_reflectance(600, 120),fresnel_reflectance(800, 120)])
def fit_thickness(wavelengths, R_measured):
    def cost(d):
        Rx=0
        for wavelength,measured in zip(wavelengths,R_measured):
            Rx += (measured - fresnel_reflectance(wavelength, d)) ** 2
        return Rx
    
    finalcalcd = optimize.minimize_scalar(cost, bounds = (1,300), method='bounded')
    return finalcalcd


def load_spectrum(filename):
    spectrums = pd.read_csv(filename,skiprows=1, sep=',', names=['wavelength', 'intensity'])
    wavelengths = spectrums['wavelength'].to_numpy()
    intensity = spectrums['intensity'].to_numpy()
    print(spectrums.head(10))
    return wavelengths,intensity

def compute_reflectance(wavelengths, intensity, ref_intensity):
    if len(intensity) != len(ref_intensity):
        raise ValueError("Sample and reference spectra have different lengths")
    R_Si = np.array([fresnel_reflectance(w, 0.001) for w in wavelengths])
    reflectance =  intensity/ ref_intensity * R_Si
    return reflectance
wavelengths, intensity = [0],[0]
#print(wavelengths[:5])
#print(intensity[:5])

print("OxideThickness Calculator. Willow Valeria Pichardo 2026")




#GUI
root = tk.Tk()
root.title("Spectrometer Data")
root.geometry("1920x1080")

root.columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)



left_frame = tk.Frame(root, bd=2, relief="groove")
left_frame.grid(row=0,column=0, padx=20, pady=20, sticky="nseww")

right_frame = tk.Frame(root, bd=2, relief="groove")
right_frame.grid(row=0,column=1, padx=20, pady=20, sticky="nsew")

right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)

bottom_frame = tk.Frame(root, bd=2, relief="groove")
bottom_frame.grid(row=1,column=0, padx=20, pady=20, sticky="nsew", columnspan="2")

def LoadTest():
    if ref_intensity is None:
        messagebox.showerror("Error", "Please load a reference spectrum first.")
        return
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        global result
        wavelengths, intensity = load_spectrum(filename)
        reflectance = compute_reflectance(wavelengths, intensity, ref_intensity)
        result = fit_thickness(wavelengths, reflectance)
        rmse = math.sqrt(result.fun / len(wavelengths))

        ax.cla()
        R_model = np.array([fresnel_reflectance(w, result.x) for w in wavelengths])
        ax.plot(wavelengths, R_model, color='red', linestyle='--', label='Fitted model')
        ax.plot(wavelengths, reflectance, color='blue', label='Measured')
        ax.legend()
        ax.set_title("Thin Film Reflectance — Measured vs. Fitted Model")
        ax.set_xlabel("Wavelength (nm)")
        ax.set_ylabel("Reflectance")
        rmse_var.set(f"RMSE:{rmse:.4f}")
        thickness_var.set(f"Thickness:{result.x:.2f} nm")
        canvas.draw()
        if result.x < 2 or result.x > 299:
            messagebox.showwarning("Warning", "Thickness is at the boundary of the search range. Result may be unreliable.")
    print(f"result.fun = {result.fun}, result.x = {result.x}")
    print(f"reflectance sample: {reflectance[:5]}")
    print(f"any NaN in reflectance: {np.any(np.isnan(reflectance))}")
    return filename
global ref_wavelengths

def LoadRef():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        global ref_wavelengths, ref_intensity
        ref_wavelengths, ref_intensity = load_spectrum(filename)
    
    return filename

button = tk.Button(left_frame, text="Load Test File", command=LoadTest)
button.grid(row=0, column=0, padx=20, pady=20)

button = tk.Button(left_frame, text="Load Reference File", command=LoadRef)
button.grid(row=2, column=0, padx=20, pady=20)

thickness_var = tk.StringVar(value="No data meow")
rmse_var = tk.StringVar(value="No data meow")
label = tk.Label(bottom_frame, textvariable=thickness_var, font=("Arial", 48))
label2 = tk.Label(bottom_frame, textvariable=rmse_var, font=("Arial", 48))
label.grid(row=0, column=0, padx=40)
label2.grid(row=0, column=2, padx=40)

def create_gui(wavelengths,R_measured):
    x_data = wavelengths
    y_data = R_measured

    fig = Figure(figsize=(5, 4), dpi=100)
    global ax 
    ax = fig.add_subplot(111)
    ax.plot(x_data, y_data, marker='o', color='blue', linestyle='-')
    ax.set_title("Thin Film Reflectance — Measured vs. Fitted Model")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Reflectance")
    ax.grid(True)

    # 4. Bind the Figure to the Tkinter Canvas
    global canvas 
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, sticky="nsew")

    # 5. Add the Matplotlib Navigation Toolbar (Optional)
    toolbar_frame = tk.Frame(right_frame)
    toolbar_frame.grid(row=1, column=0,sticky="ew", columnspan=2)
    toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
    toolbar.update()

if __name__ == "__main__":
    create_gui(wavelengths,intensity)

root.mainloop()
