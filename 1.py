from collections import defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if s == t:
            return True
        c1 = defaultdict(int)
        for c in s:
            c1[c] += 1
        for c in t:
            if c1[c] == 0:
                return False
            c1[c] -= 1
        pre = defaultdict(int)
        c1 = defaultdict(int)
        for c in s:
            c = int(c)
            for i in range(c + 1, 10):
                if pre[i]:
                    c1[i, c] += pre[i]
            pre[c] += 1
        pre = defaultdict(int)
        for c in t:
            c = int(c)
            for i in range(c + 1, 10):
                if pre[i]:
                    c1[i, c] -= pre[i]
                if c1[i, c] < 0:
                    return False
            pre[c] += 1
        return True


# 1.py


def main():
    sol = Solution()
    s, t = "3156", "1365"
    s, t = \
        "43604645359664456594625814982312218205818739155645373340148555988638657063453826047850315192093824771281290009657882118646495214224338675464539755719399900718899721293399666026018786355403388416126517521159554502054040291854158668609975664325995291942293207825733125284139366422572781914540810717214200866006489892769014002168973338294367647702345667299068463639533420068166773083013888543129294689255798813232680392826429402617511002804733482284371770883235156805371851798524070023172047795542346021094497790941142149221195896508875348504816071797280918450662692226183171931032365583601960361207604444280273470195431606963992165114782852001581014414936194130959358499508008068896783607228017972015336812345715449031967530252760631057713941049029038753113648927034460075807882959635707190601527563495045632490321889799361109560522366076063554062725283881785050068304588269135877774152159204017886655549761515907419880335953777533090429037111661787962593669395422649830918459230323894621882957970416164143983422063466229732036293557254373015434709518167038336352955098838835506814616526915881562925048957672410705902393503881916780827740260991259806382310104167506178287557846770476216261396057127884657886577390843707793042396310380447645880337185003451570799183304884869168797351870239315020907428124294996118872523940706256630357231706908515644269123168583666618354664055471585816452603982680950403626891861759954399236069238321844089077896509548895155855529786999958896569505949015836887272584641053271424847899908098435616013167213606531282168580843869951098093139422339709081881154493855704444666792511407168341987929358084395019166250229850534486673903917053607829424860538864169399867832211653604526241330465374436557626777174573879656140348794120435661487934674263069276880294957170607506215713295974998971747247094553860025408431284223011514033561447654670226605594389620569475894054376605433121733188807287075383482870962191304803021868205103847704494889121902349779202773577853841300151834585114364387897661919921298494578963286353029169055137065089207000498046168806803148406957266065865015185526490726731273293972574396533681366109930165732790573434042309702995102635395915693141798979146578279901604968429399399914215540384747197516337244451466857697862860401729919416381887717552957774485037345421920483857858498355384866844941774737012667317964781028433484246437394992608359324202860618964877462677345831369684185451107786540380830654662347782495210489956579188012647459154335136626203247057549541299373821323214688713120677872907858245508969253944839929597415827983076333374733068212937306787589802727291412904787189952307118524774731038427920037619971292627140356022257353488016244187117659572218274590623553783013323761041609768080135414036678532195883067769542787999717311777901839490534347144940064799075828540219392825940838385933141725470439608603440602684701629861475858017284894289759369092984324268764060344030718128969116105936119136555150263257457775542905204396754658379187669840053378770662864472663289760000611687626963954484824256468839639286648270224775047007368252890765091732532536462505300186045070846238806264306158309009484649848123631342928593455713463585250708380642510050743642115595396640473956521649578914815699518191685874525915737695158402826082928915600398650762581237765665122036000832845261019489204203900672001636357067808950842683928894767807750306890180801038719934569381550917505704042669840668058917042240438224586084291606645222096106776981084768746364869727415991682076536362521089445828505478665694456174892469377500504248548614085565585179615987318974764368672254289681816158378388840172371265353162145480768362912911528457932987923800329002557432711259467808164010826", "43604645359664456594625814982312218205818739155645373340148551988638657063453826047850215192093824771281200009657482118646195214224338675464539755719395900718899721293399666026018786355403388416126597521159554502054040291854158668609975664325995291942293207825733125284139366472572781914540813717214200866006489892769014002168973338294367647702345667299068463639833420068116773083613888543129294689255798813232680394826429402617511002804633482284371770883235153805371851798524070023172047795142346021094497790941142149221195896508875348504816071797280918450162692226187171931032365523601960361207604444280273470195431606963992165114782852001581014411936194130959358499508008068896783607228017972015336812045715369031967530251760631057713941049029038753113648927034460075807882959635707110601527563495045632490326889799361109560522366076063554462729283881785050068304588269135877774152159204017886655549761515907419880335953777533099429037115664787962893669395422649830978959230323894621882957970416164143963422013466229732036293557254373015434704518167138336352955098838835506814616526915881562325048957672410701602393503881916780827740260931259806382310284167506178887557846770456216261396057122884657886577390843107793042396310380447645080337185003451570799153304884869166797851870239315020907428124294996118872523940706256630357231706908515644269123168583666678354664055471585816452603982680950403626891861759954399236069238321844019077896509548895155855529786995958896569505947015836087272584641053270424847899908098435616013167213606531282868580843859951078093139492339702081881154494155704444666792511407164341987929358884395019169250229850534486673903917053607829424860938864169399867832211653604526241330465374436557626717174573879656147348794120435661487934674263069276880294957170607506215713895974928971747247094553860025408435284223011514033361445654670226605594389620569475894054376605493121733168807287075383482870962191304803021865205103847704494889121902349779202773577853241300151834385114364387897661919921298494578963286353029169055137065589207000498046168806803148406959266065865015685526490726731273293979574396533681366109930165732790573434042309702995102635395915693141798979146578279901704968429399399914218540384747197516337244451466857617862840401729919416381887617552957774485037345421920483857858498355384866844941774737012667317964781028433484246437394992608359324202860618964877462677345836369684185451107786540380830654662347782495230489956379188012647459154395156726203247057549541299373821323217688713120677872907858245508969253944839929697415827983076333374732068212937306087589802727297412904787189952307118524774736038437920037619971292627140376022257353488416244187117659572218274590623556783013323761041609168080135414036678562195883067969540787999717311777901839490034347144940064799075828540219392825940838385933141725470439628603440602684701629861475858017284894289759369092984324268764060344030718128969516105936119136555150263257457775542905204398754658379187669840053378770662864472663289760300611687626963954484824256468839639286648270224775047007368252690765091732532536462505300186045070846238806264306158309009484649848123631342928593855783463585250708580642110050743042115495396640473958522649578914815699518191685874525955737695158402826082928915600398650762581237765685122036000832845261019489204203900672001636357067808950842683928894767807750306890180801035719914569387550917505704042669840668058917042240438024586084291606645222096103771981088768746364869727415991682076536362521089445828505478665695456114892469377500504248548614085565585979815987318974764368672254289681816158375388840142371265353162105480763362912911528457932987923800329002557032711289467808164010826"
    res = sol.isTransformable(s, t)
    print(res)


if __name__ == '__main__':
    main()
