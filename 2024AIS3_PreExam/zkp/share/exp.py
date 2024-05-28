import random
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse,GCD

# 捕捉的數據值，替換為實際捕捉到的值
a1, w1 = 119302766539406035588684007531054567525950650559292683835949015322246901459744362590367280386351404352826746744012332124300942180729540602708698130028811227381889341361028776801585136416157903095064052268200844806527639455476518182466302042710296543386864938958757088323675716961730189883233811499213875332542,159517778957314375570308656495901256036979249509269140355771574933198071664338160211598490394606301957225453316749460320984298485579330408004038854738878914333910882991828180501526695921448246344761806599857811604328995165221367349188556951856883874674360081503991095779256710830306042236788337630528882811783  # 示例值
a2, w2 = 119302766539406035588684007531054567525950650559292683835949015322246901459744362590367280386351404352826746744012332124300942180729540602708698130028811227381889341361028776801585136416157903095064052268200844806527639455476518182466302042710296543386864938958757088323675716961730189883233811499213875332542,501277367630354145368594154748527213746271472139099365602663973552610168433294417553526572518451836203961466332843535327080134215662823765719489768622852327019560619813654516915936544402713712098385535446844316355190078790816002569666707418641060026579618409789125217896499133282526198754849406689054213050748  # 示例值

p = 912963562570713895762123712634341582363191342435924527885311975797578046400116904692505817547350929619596093083745446525856149291591598712142696114753807416455553636357128701771057485027781550780145668058332461392878693207262984011086549089459904749465167095482671894984474035487400352761994560452501497000487
def find_coprime_c(p_minus_1):
    while True:
        c1 = random.randint(1, p_minus_1 - 1)
        c2 = random.randint(1, p_minus_1 - 1)
        if GCD(c1 - c2, p_minus_1) == 1:
            return c1, c2
c1,c2 = find_coprime_c(p-1)
print(c1)
print(c2)
#669941972288872336272981622216378931554294186011895765864571540364321019680808100315185231739241246726671172687774648801762157689501280750045910461229970844930605666868846978452042248050152199173958524084715676059018639068069045759298477942355177278744650809515404593534162901250657591322856515383404251373719
#277906741529453588700567124899696467757103188704147536992780621201155209317086022880093072868774861121968890614548234881290227064034488720398423672475202670527917276883595125751326687788075311829395095166336710337461038588498312647854047853727391305719656003211299106358031120224111626774770801741380193444226
# 計算 (c1 - c2) 模 (p-1)
diff_c = (c1 - c2) % (p-1)
diff_w = (w1 - w2) % (p-1)

# 計算 diff_c 模 (p-1) 的逆元
inv_diff_c = inverse(diff_c, p-1)

# 計算旗標
flag_num = (diff_w * inv_diff_c) % (p-1)
flag = long_to_bytes(flag_num).decode()
print(flag)