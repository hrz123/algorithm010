# 1044. 最长重复子串 .py


# 定义子问题
# f(i, j)代表s[:i]到s[:j]的最长重复子串
# f(i, j) = if s[i] == s[j], f(i, j) = f(i-1, j-1) + 1
# else: f(i, j) = 0
# 初始化和边界条件
# f(0, j) = 0
# f(i, 0) = 0
# 返回值 最大的那个长度
# 超时！！！！！！
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        right = 0
        size = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if S[i] == S[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > size:
                        size = dp[i + 1][j + 1]
                        right = i + 1
                else:
                    dp[i + 1][j + 1] = 0
        return '' if size == 0 else S[right - size:right]


# 二分查找+Rabin-Karp
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        import functools
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1
        n = len(S)

        def test(l):
            p = pow(26, l, mod)
            cur = functools.reduce(lambda x, y: (x * 26 + y) % mod, A[:l])
            seed = {cur}
            for index in range(l, n):
                cur = (cur * 26 + A[index] - A[index - l] * p) % mod
                if cur in seed:
                    return index - l + 1
                seed.add(cur)
            return -1

        low, high = 0, n
        res = 0
        while low < high:
            mid = (low + high + 1) // 2
            pos = test(mid)
            if pos != -1:
                low = mid
                res = pos
            else:
                high = mid - 1
        return S[res:res + low]


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = (1 << 63) - 1
        n = len(A)
        lo, hi = 0, n
        res = 0

        def test(l):
            p = pow(26, l, mod)
            import functools
            cur = functools.reduce(lambda x, y: (x ** 26 + y) % mod, A[:l])
            seed = {cur}
            for index in range(l, n):
                cur = (cur * 26 + A[index] - A[index - l] * p) % mod
                if cur in seed:
                    return index - l + 1
                seed.add(cur)
            return -1

        while lo < hi:
            mid = lo + (hi - lo >> 1) + 1
            pos = test(mid)
            if pos != -1:
                lo = mid
                res = pos
            else:
                hi = mid - 1
        return S[res:res + lo]


def main():
    sol = Solution()
    s = "iuiielmwbuhncfgvnsnwwcnzgbuylftyoopqrmkbycbubrvrfvwbufeooizjydgtpuxwpauqklqqlflzizazpevkcqysqyxhxpksvhnwdfaxqbpokvropwipxjfxcohnxvkyxybgzprkpsxmwuzdgfpaimcprhvmmqvijkfyrznhoucelkyoogemciorlzwigbvehltglnxirtedwhcxonzvbevluqpdcmmbxbdxdcfwdsnbcqbtuindgtwfnoadpchnzgkaeyjaonaehuyscbgnmuedyligijyeretyfubaazkrsexdbmxdhgquyvcuxyhfufejbwfcgurzireoprfceghntuvecrkfolanunkhigeqflufocnxjvfixgkjnbvoxwizvbelwhcdugmtohuobyrjesztnglsykfsxnikagckszybiuywwsdzomvaukufdcaeamdlblfixrflpqybajdnyrbasqegunwnpjejvpcsonfhqdzmhewdbqcdsjpcsvhmdprqujbsapfkzwwikfcdzhndnelhvnqilrtwbnzytsrmfpevqrupkdxliohtzbunzeyqskrvasycpzjrcwzywtqnoljzzkiarptcixcewpdqrcczchabvlnwtnrqxsvygrbpncfenkgojvomyrkqcxjzmxpsdofriwyljtwpibhfkvkkrnnfpbvceqrrustnplvogqyjmkjadalslxogdtuupzmdgkcjridzmpcldmgxrolnebxaodyshachjanskuwnsljumqrudjrjipequhqwxgpwhgnigdemdjsawvukqlamxxzqiavunzpkpuogpoegdhvxiedzvmhbxgqlhhwjlqexbojjnnhogktvedekmynvuzonqwwyntacpawlwtxsajrkzcivhnaukxzgugwdirrgwofasmdhduyaakqclvzltrdlwhimpvmwgeebvxfniupaxpkaqnlzpesurityfslpbdtffbqipbmkxfarpgteuwoaabyoqpkwmpvyarqzrbidzdcqkiwsgimtgllkjrgbzzmkogqsmpoglbqanilcqumpqotffhdymbjuftjwkljnyqpxzqffbncifmemtkxayaxzslfatiwnrtjdiyknzxecwrabvtoypcsaesmuvqgvkrykynxwzhyuurykveahbehtplvuzjxncegdfjpjlglfzwpipehksjswqiawipwdugltppqbujjopitgrtpslxpsfaanccsqtyuypztsplpfxxogycjpwmckdugknbcbbtjyqltlhtmtpdolptlrhaxnzchtlohcvgehkhlbewdcqswogzbjjzhlkheyamljyudwrfiqvfgekbtzyulwadkgdpflfxvpshcmlvrzzdgkdelodppwjyljmedrmhsfozmtciduaebpjaagykojwlrxrxqdsjvohrjzneqbfnsnkjxiguyuprrqzbaxpdrurgzhwmfylkmuxouasuztymcyzllvbcrxfjmwhcxdbgdzdzevftxabzwsisdwpvjauaqarkjwhjciqxckfmeqdhuvjljtrsieqkltqxgojmiqmnkxiedqowhnsrfwlcfdmwglidgcgvpjnfnqncusbfcdqhbrxqhslpxxynudulzfvvachayogeasyalhmwbknrkynwfhriqvhzykdsahlpfeoppkecxaxltkkygknvqrdpaikbzzlusnslcqxqojojytpagkfbiyezpbyfjgixqyzcqygcvwqokurblqyzqryfjdeeflqgworjltrfpkmtzafvuhdoqizyhqtzbpbvlziczhkqxcbdbxfiwsihytabcujqgyguxkaegmrnrasnolyqorspbmyanndarkhlxcpzxrznuqlligznfuivhmkmfdesyeuwelnoikbzhwnaltruclcchnximwibwtwjdnqofvlvplvkireoxorwqlcytwiiajbalhawevxwdefkvaezhfssbkytzrjwkurxvcxhhblgfcyhoubsnzlsvganxijgecztbklughbtulvwwkiizcjtadhmkbrdrqjcyfmmilriznqrmywjtzzzlsrgfhgoqldvdirohuqznwatmcoygzopqbcwgnsgdrygpichbxjzxsorzzkhuaexziyccrgavgicrazujbsgsloufonaydhligxlatxvcinnjkncsvngsadpghwxvzfgmanhvkvwhenvsedpqyqnqvutfydppubsjsgbqrbruhpsrrpcsmyndrcskkgibkvbvelljogfezszbgcjoppnqhzmuvnjvwtmkggmfiqwwbnnpylbqdxtmfsdwsogyvsqwvpczmcvahqqwtzykytirguxjcqsgrplqytzaojsuxycovdtfyxwimxbgvzzvmpitdxbhkegdocgapbrfrvjsormzjswoxdrbsurorqqrquhzorxmypygfvjdwbxndpzveqzoiflewwhmygwifmbpgfvkfmaiodfwjmgejlwgytdjhczbcivwsppuqenunwyyxtcrhxonwywpgpqcujzlflplxbocbpmoivakwsevzxggatdzqeztxrkkyjaugjexinqedxtkwykgbnyumjkrosrllqrryhanlwegnfordfexagdbafjstqlzoluqaxquhduyqwmeeimmgdraosatsjgrwygcrqtweieafsubczzxhixrrcxmiwkqjjtgzhblszwiwqjnxoprxsycqvwckaczjfxbrgaoxfujnqqpwehgtucczrdqctaibmccokvxdyqpxmfnnlbzwkmpgfjhcusqnkipkodkpoobbgrsokfjsyqtcknepyevfsdtdidrjztugtlcqzjgupttcktbslevosvbgxmxrbsvkuchcgxpdthtmuippirutisdiwiomubzdqosqdsnnszgatbnhovpizmbbjgxvgbxiryresmfcbswsgcacimyzjpwmxsdigibckikxeuixbbzvnwljhpxzwrcettnzfdsosvfrkcaxghlqgbsnlucvyfkbpmuniqdypguiaqswxrrzfhoeogjpwzztseqmoaksqgdtgcswoqbcrvwztprnsodzlrywzlgcsgwxeloiyvsstrhityqeukvocgoytrjbrusiovgxqdshesupvpecziigkuyjuwqpagfovhaeurvdegwtkphppinfacgngghiqflknmvfdycwqbqxerhguqnwzjxsfbwwqbjinqvgsmbgldgqwkokzqlwdyzhtdqccwtydtpqewkatinmpdolyosdacsmpujeyfwrhvqihorbgasfzpujvcsymigqlqynuotsomrlwxywaspgqzkbfckyipzxjrjrbkqluwefgjjkpkrurwypmsvxmyqnyqonplfwnjgynrkjodvmazdjyiqiwetdzjyaybpgjlddkncljpqgtpkgoavbbwbbbndobbcbaktvwrxbxulmknlzwgdocnngwmkezhdcnbkyjgtbubvtbntwqourytmldlxmbxxrndximtddesbguqyzdwykifnsbchkxwlsewcisrcseipfjohzrvjxqdqbkafzahqiwjbzpbwdayygweaoovabtiqinibadluqvgzxkuiqgulcdemfgltvaqbwtuyoqxwqdurhydunyqniitegfcrknwvubclfmhqyvtnwmuoypwzchjopoguwythwrmbtymcnxqvyojlirkvlzmebmscjuwgqhkfqnwcxhrnhprfaamqiwrplvdmxdfqfiysqpwctuqmggopuzqbxartbjlutpycbgsfrtljhwftutnaawqruozfxuqjqomschcagdxxpgwejrotntqlgvsrmsurxigmxpiuretciynfcbejaqtpyjlbgilvepqndybefvhcdiujubrwhikmodthnbxixlunuwqgribmodtyxouhyafdlqeskmeuoyhakttlvpyqxzydrhwgrtflsvmvsvtidugaaybvuerlrgbxjkshxtiplxsyhcnncrchkeumqjhusubuwaketwqpmowjvfwuuzrrpgekxmhkglmniocmziucaqvirppcjucqedfnjfyaemvxzwuzzyeziwbvalguyezjilqekqbqhkgbgjaoilrfstvlvmoeenlicatngpvrtuuywqpeemnnvgtevkxznicfjwdbgclxaenbchgqnvomhkaafbikujrbnjqfzvgopcnlujejmcmdvbtxrlrkyqtayhgkdyrieyuymnofwvzycidrhduqlmbpuaztkmkqxlttvibhjwdgoaljxlxcjiitkjyemveqhyjvgfnprceuijcfxrctjjtijwzwxbxmdsskocxtdyvqsfjdlafcgpbwijdirvsujfezbfewtwafmnrdvqegivxmyhcttkbwjffqphjcoackbprrcbxevwqwipqcqzdjuwpbrxymzibmuriqabwtsisijildsuvmsdlteywhysfavlpyptjhccnkiugzzxurqcepuvhddjdnpbidexqfbzkskmxqfcfxzdqhxywegnlevxgzkfwyyebkypfamodeshsispcbegwbjjbalcdpuviysvppknfhawynczychthbojmyjiihputdlnrnwgsgiejddxfpnayfajtugctqnkfrjarbkzrqrvtlsgnqqmvwtpluzwtthkiomnnfdjvuqajkarcvkpwtvzjariilatklnshsqdhtiejulcvgrtxqodsgoimpcyypsnxppjhkxrnstowomqqgmosisopgwnjaypvmtuibypfuduvnjqxamllbadgejvqroazkpbqzvkrcsmjnmkkftcarhqaqfzuaqwlixhemwglmejukgthqjocckbrbmhqucrenfqoekrroekxafvlzutdsscvcbitjuztwkblfyaxirptulfvrmmthijxwlzuytxoupzvvmkvdvntiawdfhattosqhasuikocyqywjohfqgvbsajuqfwwzxywkxsntrggwxffzlxzhlvhyjiuvhxplnrqlpqudoleljxcntsjsngmyehrwwruvwexkyqbbhlvwdojprakqahdunowuyaoqmnrzabxqbkfwlzdfxaebsufrogtoldnryibgggigtfmfyjdynxwmwirrnufbwpkgdqhohuhozzikjyngireqnypatlqscdreveyzrpwolcpzmxopwqpfejtutfeqaczjtzguqvznkwtsztgfimbazhixrvtyowlvhokmfgxlrfihxaucezqlkupcccdyysydzwoftbkxelotvlnquwqwkoxxiauntglfuocepewopxdeadkcghdscqmejdwgijdcejervtsiwndjqjhccotkbatjgxyxfkzbyyuqtjvfqjmevhjmxomaxwiapcwzatorslgagjtykmwegrbboritytawndfrymzjmqawlwytseugxhyyijxofallvshguvdxuzaqmzzoqrwodkkrsdhwhkgemsktxsrokcablkybfqbllulxqpkkwswmrxnznmtknfdqarvgvltojfismrvfcowmtrkdcqilucjslnxdwyzayoxejmhjeonzwdqpjjovumpkibgcmotazussvaofxnuladaghokxjntfqsdybvbwcyhusfdwbpivpvuxxfwbcdyvejkfzvnbbrohbswnhcwfhhylnsnayzglbirrdjksrxyeyftxmuhagnufhzyhaniersbdtjdsrlbzpkoyeehsgmerfqgnltzvywoeldjidhjsakcnjbvgwdaocxxvgyjjkigkrnpvwkzynbpziatncmmlharpqwqekvokamjiuptfirqhijulebypdwriwlwdjilenpvjpusftctulbqgduqhfbmgvylsmzmpczxlbdqkhdeeexiyxpdfpzynltvnptyfgyapooqcbgluqvgdopoyrhhbdmogybhljnfhcrehetpszeaohtbvdamtloaxrpgopxyennxavrsabnxdxstjyhcdvzhfgozitgiennalbgrefilibegrfqedmniyhhvttczrkgmuwiasqykoazxpxmczniyjnopyqtvvrquztexhmqztarekcunryrvptokmaftaksdqeejtdwnyplgbmencrcygdmenxxzdstwcbccxatpijavxxnxyflpnneeagysquecbjrvyoogborlxrybpydsvkffseqyeevcxontmqkmlpgqsymwpquizbawjpqpowyomficyahanqdazfvnaczfcfgoedtttdfaazknxycqynstwixfsdushmxmtjqwcuktjmcnyzsncpblmcnbnhjbxonazdpsrvyjcuxymenbsjpacgveuwsmikyieyoavdyejrwygyuhrvjwuydvfcjxxrvuwkncpfqucitxnlpzzxdudlxdgezetdsealhrmllajnznfnlanobgjxoxsdwfcslpeqmvjnxgecvynvkwiofzmfnqkthbxlfawyughefssnzcoaiwinrbqmztkgkcuzvsmxsvudsvdsfknyzhdastxikmhfrvfumteremzkfevrfdvjsebmyzivtexdhsjrrmwjeevktcmlbtsweygbnydwrvzoynzlcfbbhqacqqakubzgwstxenfiggdwsrnkkvfnbayeuzwulzdhmrgpxktnvleqvsdakkncojammomwgjnkoalrzzaijnpsonjeipgxxcglvosgasyifkoymqvhlzsqrhonohhsqxjaqswocmmzlftxebazvojjaijthbavdcutwekqboqvufpjdmcbphvjovexrdyzwefwzzlazqhbubmjlduzfvytpdxkkxhycynysxzomqsomfcaxaxtqbnabwbycgdeqwtmclkzuyyuzqhpjhwismgutwmrvlsbtmirbjivcyjmchlvyflxvdjdjjuevofvxchvqcnifakvnmvpqdzusxklvzfwihejnhxqofbmoisblanxdftqerkxcrgfanwsqnnhpjqwhequlvjesmymayqwomhajjpzktfbbqdvrnfzherypszsmxyixkfihwfpjfsljaifzzyfsoxpikgewuinlwrvgohgfqxxryrxfvxkhgtcpqcbgeymlfydkudegopfgnpjkrzsbloevpdyxbmhtbunpiiwfjpyoqojlepyqaajqjbhnqlsnvcwdryulrhijiwmlimbsafhcucyhzhgipiahnzkwiysutzxqkxepddfckgmrdiogjsftnvpzuhhatpckrodafgvkvkcqzaozbqkdsfzzpdxfbqtcjgejxftphontqnsoeeiezewjdfzuuozavgkspsozmrvkhebfunmdlecdojzczqyyyzcyztdvykmoxveqexkrxzrnqeyjmuaxaapsosqczbzybwnqetmmybnzlnsmygyxbupbolxbudxvazsdtkrbbuvylxwiyqviwtafgbfefkjdrocnfxwhhntmfrrexetmkadfduahzqdnpujcxfrokgvhjthjnbwbherwawknaxvmfrflraapevvmqodvgbsihtucirswpheqjxzpfldjioezonporgokkgiaszhcudfeecvrddieorjmufxftcztnxafnlxkmvctyetbplblybieolafdnztmrhcgzmkeqpfmbjbuobtjaodjpdvaeomoknrappaibtrqezxamrifufzowfkwdjepalxujaogrfgxnxsskkxfnhtfvgwdrrimsumxzcqqftsqywpjhqhudnxsxynuxqgzcwpcltluzymkbefbsvrzjwrnljaceisidppyhjqaydxaslioetbjtanggbhqkdnhzsgzqbtspkmteoymvxsnpdsaxsgmkgzidqcwcesmhjpkvppzmsdgjcremrvbmkllchrlrylcjrvclszbmjihppjckszfobbcqqpxgtcphndampzwcyubpuapgitlivdhcmkoeuyecrbpiofqnrodlaxwuyendreinfkhvnadnkiqhzpdbisymulfhgoyvzvvafxzonnlplkiywodfflqccmlldipxztimfzpvczqrmggfjguayqqvuwcerpffijttmggfkgnnhbweosrzenmkmhvzizrxrwhkwarquiqcjcbcpiyhyvddfvqpsxyoipaufjfxosuslehiwisberbuabcufajdhyheaghjznvbphmegnnikmtpxgxlbkxstvrdyvmuysnnmgrjbdiixknockznluhczbgsqwtsxfmcfbohncdwwhnfkiadefzffsbqaihgukavwdhebcwzuvqcsdwaubwwpddlioysxrlcdpzvwhfpnncuesxxftujqykgtuvejgnqnnrgusurlltpcjncxggbcpmwonoeloemjugangzxhzafkckiwjixvtbvkqeuxcouzlhqepencswgdljewlzrmmlktatczgknvpjdtjrdyvrsorkrgwvxgeshncmwjcmbqsbckkedxnxcxeoqnufgdbiltqklmepsbvdxqyxosrxgyghohoherenqqkcdpshcgnvdsiaqgbxoiwbnstulorlkqtoyofbdiwqqyovaxlxwqoxaukjbdwpcvgooibvkojcgkmopqugackzatnfmfcdaksnnzcabghdjlpqgslkrinljntnyuxesiiasvfvpnsagrtfkhxizebjffnynslylxqhrvcgrbhpplbadttmqdymdurzieqekizqkzhmsilrtnbeotnwwyltbkiahdderkiedspilycjvjfdmggvfvswcddpqtdaozpwfycsefpqicbusqdhucbndyttaypybxwdepqcgpfnvljkbocqnvsewciqewxxpbwbhawputrnkkqtpbcdytidiebeykrppuzrhycmhgzhknfjdzkpfhoxrswedhnvnyxdtxedukjirboigwexslnbtisyfbiurqkiitlclrbjleborreizutjsnsjvcpcyhuginhnnhanxjsdnjbmtwbesuecdhdemtjskvitfqmhhgtflehrafopgpakeswseinhgfpgaavosthlbffwgmkguoyyrjeyhtkgsegrbmubhfimernxhlhcdoqdmyhuxzkkyjruehkqocfqzobczljhcucvbzbivyaihegmabccfbkmkaoezugliicoiyrfsqdzhhwhxynpjxjsnkbpvytyejoctzqfjafwpfnprtnhkwknnrikpylswgszrgeffvroervyofynycbzgrgcdpanrfeyqbxgngzkbhdagzfhnpnvluakfdhfcvogyuraankndrbruhkzhmxzbhmvhmtakmsoozuawedlmjhhuvbmeyhdnhtacddcgsfuadhboinhzwmknyyvajtrzhwfwqlvehnjxckdjsybwhsoatyjklznwxwslmhzrdaxowfghfiolupjbmkdimdxwjobbrnuyendnsbahjtkbxgddzlkkdaflakikvcwivzhmrgpfckymwtnwlzrlnthfliwpdcpwtloajgyjpdgleudwpnouiojbepkmgvgkelhzcyutnsapuqkamwkpiextoytjiwtpkbdkqgltwsfaunkzogrbckhxiabwrvpmwrpoyuwgalbkgxifluysrduuzqbtemnmfcegploawzsibbqnyjwlflsdwwrnlszgmypbnhrqxcyiwlkkqfvqumeywjssnhgetejzukgztzrmvfajyraawogpozyuarxhcurnzxdsbnyckplrkkxwwcjipbwfqbwtapyhlwlowxdebbkpimustujkxyqhgxzuiaddubuxyvosfkplgimcpkosyyabyzyuyjxzohhctwelxtemvfsvgdmyktvvxzhftjvxhwcayhudrsgjmbhbxnecydibyeegpjzgicteyylbzjknqhohbmjqziupajbtiiugytyxduzimyspucowurhjujqxodbboknjnynmosftdtaxqfyteimcelkbryjnzmznpnshcegempkyyldtzlnpwbcypnphlnwtxmvlhbnjxmbbockwghzszbpgmhsiebxtwmndnyiaoqzdhgfzuakykqmxmksiqtqusbsbpntnwevrckjarabrhncjrqytncwvfxdfmntuoabminszlpjotflublgqmsubxbskevjzsdamfmlmzoscrmqnufjermnvlzlkbbipehuenispznvzpilcjrtflretqtrgwgtsdadbyfidxowihvdvqiidhzzmmqmzgjiedflvgtlscaumeskqjaoczhaopsndkcpleygaxbmglxxyhphrbypbroaxntjzuovpmtahmuxnynafjizuknpjwwtdrvqbmqlvpaxgtvjjpbxygwhawcokxqlderwdrtgvtnhkbvpzhjiqoccvrtwwwfbxsdttudydynaupqujupxtiaxpvgfremzrbzdbcxqjchkmpzpzrqomrfnhslboovebwqyqdmqppvxdkzppzcrypsxwdftquwwbkokyjserfjcprcrjdvcscgmauarjajrkrerszolcwxlkufnuuwbgbmhyzqsnhbkrpqdxirveddvphjaaxrcpfepexwoxwuxkjczkcfqfqyghregbciujqtqoiwyjfggmngsohbzgpcpwsfubvibqzblriuyddykexycnkmbmfzubbdyaqvgclvgngrlodpeayjuiwcfvfggnrifgzbfuywuhdlqiluddrxdmrsuojrulcttiwshoekpgyqxijiwlyjjsypqllcgizpxkhyghkogksxauylbntfdfgotoncafqwxsjyblhdujzmtbtqlkzrxpjpqsglguydkoghjwroocjjesulunomntrltllpeiqtnsghcbnfdvcwfrzvlmxanktjezkzksewpvbaikyvaakygdnrxgsfjnwzkodpabijhxugtgololojikptabzdbbqolexhlgljicwpvvbhaegjacahfldtfgsfizlyyvydzmjskemupxolalwnmygzrtzcprngffhndlocuksjebdbbtlphwpljhpiwjxdjptsljvjvnleigmkotssxspuzlgmqvdkwazpzbolpkushgrwhjovhmkuxqzmdtcbbhtomjyqbwugodehtoofayipuvxzvtfwitxmyfisuydmtxxpadqwxuvgetkyjccrcqmomkqhmljtnxpsizoblkkzgscxeudbdftmmhysgkngorlrxvrjbpyaubslahfmjjopzitkwtennnvkmfbvkvzcfhdbhvwmwkxmhgdbevqdudgqjczffulfnqqvakqqycjvrdqzvzpzerahrhkbzkitbzdmzruspqrtbzpatyoadrblojebbbrdsxgtedjqtiizijvjhjgfqqqltbornlvdkhslkujnoxgsfzwatwmeyslbmvayyhexjqihfpwjywfudkqxnusvyzlngenlgvtfldfzqsnqtrnoxzmlrmmzhiejvtzyyvefspdvbefdvxczuroqrphvdggavvvymkzhceauvlughgofjrcknkwcolosyjoxljvzjrhtaamblyslwrpzzwnwbuolpbewokwmarfnrwshmeyeeyqmuvnwyhhmwagigwttijiphcusidtefsroouppraododegmnuxxkgpzhikktosefauwmkllaloltkfbndfycmzmhvayxpbhpqiuillubqkkfxrkfhuqqhijfkxvwsztpvlbhrgzwpfjnceqlvrddjyfjjicfobupseddhpqerjugaluujzmclrnjmyfveujgprzhykwtllvovrphlxfywtkvvaixwostikokmydrbvmjpzqaybwbgvmlfdzpzuczccsbdooflhpjksrhqbdclmquraewubcpyswzfwwtelaweqttmmiasfkebfdlttjpulvcvekzwgntroogeaxeskdplmebafuagqjbmpxbrikmsrjamwkdhufpohctgsqytayrvhwtcpewjbodxcxpwkrqoemvmtwxrksxbimxwquwhhofciohgqtxxuqkcojaugnyhuzkttkjhsvupifkvhownbfrxcqlfeioglfihprxnmvpekepjigzwfhdsexhpjuafrbldmxlcrjssvjzpzmaclxvdwvneplkkvbxpqndqgbtvacgqnxzavxssjmjunwseilskdfnvtzmljplmjemgecumxttmfaswqclptipxbaljmfwjvoymsmwgzewadhycyycppseourdsfalacwbatfhgfceesctmekvtpdkqqgswijasdzfzwbjxzjtskvhlvbyimfzqukqrkzjyrnsaryeytttcnslkgsrtycibxdzgtorgajqfwibriticzfywlljfxyyufoffsdmaufgrfrawtdqserkjjemdgbvldyaothljxkeyutocfbdyfochjoxldlzyoefyskvcyvyuywqeskimbtitmovswieboyimigtcbuqgwasuvpxakweolyjfxqzxqntmlxypqesinhbspaekwdncciydxkbtvkqczdaxsvdnbkznwhirflizzbkekeemoghlizqhabxaifksirajlgryjkmqetumgbvvgarothabinftqkywrhdelgabkxopbjurwqtsoamapqpfeslprcxbmpszglupdlwwjofvxjvrrrsfqwjvztymtejxgdfg"
    res = sol.longestDupSubstring(s)
    print(res)


if __name__ == '__main__':
    main()
