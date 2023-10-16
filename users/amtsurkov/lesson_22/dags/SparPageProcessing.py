import re
import urllib.request
import urllib
from bs4 import BeautifulSoup
import json

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import history_api
from openapi_client.model.history import History
from openapi_client.model.paginated_history_list import PaginatedHistoryList
from openapi_client.model.patched_history import PatchedHistory

    
class ListPageProcessor():
    def __init__(self, text_page, url):
        self.__soup = BeautifulSoup(text_page, features="html.parser")
        self.__url = url

    def list_dict(self):
        ll = []
        for e in self.__soup.findAll('div', class_="catalog-tile js-element"):
            list_reports_data_title = e.find_all('span', class_="catalog-tile__name js-cut-__text")
            title = list_reports_data_title[0].__text
            
            list_reports_data_price_sale = e.find_all('span', class_="prices__cur js-item-price")
            price_sale = list_reports_data_price_sale[0].__text[:-4] if list_reports_data_price_sale else 0
            if len(price_sale) > 3:
                price_sale = price_sale[:-4] + price_sale[-3:]
            price_sale = int(price_sale)
            
            list_reports_data_price = e.find_all('span', class_="prices__old")
            if list_reports_data_price and len(list_reports_data_price[0].__text)>5:
                price = list_reports_data_price[0].__text[:-5]
                if len(price) > 3:
                    price = price[:-4] + price[-3:]
                price = int(price)
            else:
                price = price_sale
                
            list_reports_data_url = e.find_all('a', class_="catalog-tile__link js-analytic-click")   
            url = ''
            if list_reports_data_url:
                url = 'https://myspar.ru' + list_reports_data_url[0]['href']
            
            ll.append({
                'title': title,
                'price_sale': price_sale,
                'price': price,
                'url': url,
                'source_url': self.__url,
            })
        return ll    

    
class ListPage():
    def __init__(self, url):
        self.__l = []
        self.__url = url
        #print(url)
        try:
            with urllib.request.urlopen(self.__url) as response:
                self.__page = response.read()
                self.__one_page_processor = ListPageProcessor(self.__page, self.__url)
                self.__l = self.__one_page_processor.list_dict()  
        except:
            print("Error url =", url)

    def list_dict(self):
        return self.__l


class ServiceProcessing():
    pass

class SparServiceProcessing(ServiceProcessing):
    """
    when we have many ServiceProcessing, we nead create one Modeul with configuration 
    """
    def load_url_by_default(self):
        self.__urls = [
 '/catalog/Super-Pricenew/',

 '/catalog/aksessuary-dlya-sporta/',
#        ]
#        ss= [
 '/catalog/aksessuary-dlya-uborki/',

 '/catalog/aksessuary-dlya-volos-3/',
 '/catalog/aksessuary-dlya-volos/',
 '/catalog/aktsii/',
 '/catalog/aktsiya-ot-sheba/',
 '/catalog/aktsiya-president/',
 '/catalog/alkogol/',
 '/catalog/antiseptiki/',
 '/catalog/avto-otdykh-dacha/',
 '/catalog/avtotovary/',
 '/catalog/aziatskaya-kukhnya/',
 '/catalog/bannye-prinadlezhnosti-1/',
 '/catalog/bannye-prinadlezhnosti/',
 '/catalog/batareyki/',
 '/catalog/befstroganov-s-shampinonami/',
 '/catalog/bez-myasa/',
 '/catalog/bezalkogolnoe-vino-pivo-2/',
 '/catalog/bezalkogolnoe-vino-pivo-5/',
 '/catalog/bezalkogolnoe-vino-pivo/',
 '/catalog/bezalkogolnoe-vino/',
 '/catalog/bezlaktoznye-produkty/',
 '/catalog/bliny-so-shpinatom/',
 '/catalog/bliny/',
 '/catalog/bolshaya-upakovka/',
 '/catalog/brusketta-s-guakamole/',
 '/catalog/burgery-monstry/',
 '/catalog/bytovaya-khimiya-1/',
 '/catalog/bytovaya-khimiya/',
 '/catalog/chay-1/',
 '/catalog/chay-kofe-kakao/',
 '/catalog/chay-kofe-sakhar/',
 '/catalog/chay-kofe-shokolad/',
 '/catalog/chay-kofe-shokolad_1/',
 '/catalog/chay/',
#        ]
#        ss = [
 '/catalog/chili-kon-karne/',
 '/catalog/chipsy/',
 '/catalog/chizkeyk/',
 '/catalog/chkmeruli/',
 '/catalog/credizemnomorskiy-salat/',
 '/catalog/den-posidelok/',
 '/catalog/desert-iz-khurmy/',
 '/catalog/desertnaya-pitstsa/',
 '/catalog/deserty-iz-mango/',
 '/catalog/detskaya-gigiena/',
 '/catalog/detskaya-odezhda-noski/',
 '/catalog/detskie-molochnye-produkty/',
 '/catalog/detskie-napitki/',
 '/catalog/detskie-tovary-2/',
 '/catalog/diabeticheskie-produkty/',
 '/catalog/dlya-detey/',
 '/catalog/dlya-doma-2/',
 '/catalog/dlya-drugikh-zhivotnykh/',
 '/catalog/dlya-immuniteta/',
 '/catalog/dlya-koshek/',
 '/catalog/dlya-kukhni/',
 '/catalog/dlya-lichnoy-gigieny-2/',
 '/catalog/dlya-malenkikh-ledi-1/',
 '/catalog/dlya-malenkikh-ledi/',
 '/catalog/dlya-mebeli/',
 '/catalog/dlya-mytya-posudy/',
 '/catalog/dlya-piknika/',
 '/catalog/dlya-pola/',
 '/catalog/dlya-posudomoechnykh-mashin/',
 '/catalog/dlya-sobak/',
 '/catalog/dlya-stekol/',
 '/catalog/dlya-stirki-1/',
 '/catalog/dlya-stirki/',
 '/catalog/dlya-tualeta/',
 '/catalog/dlya-uborki-i-striki/',
 '/catalog/dlya-uborki/',
 '/catalog/dlya-ukhoda-za-zhivotnymi/',
 '/catalog/dlya-vashego--immuniteta/',
 '/catalog/dlya-vegetariantsev/',
 '/catalog/domashnyaya-kukhnya-1/',
 '/catalog/domashnyaya-obuv/',
 '/catalog/dorado-v-panaziatskom-stile/',
 '/catalog/elektrotovary/',
 '/catalog/fanshi-1/',
 '/catalog/fanshi-2/',
 '/catalog/fanshi-3/',
 '/catalog/fermerskie-produkty-1/',
 '/catalog/fermerskie-produkty/',
 '/catalog/festival-tsitrusovykh/',
 '/catalog/frantsuzskie-tosty/',
 '/catalog/frittata/',
 '/catalog/fruktovaya-konservatsiya-1/',
 '/catalog/fruktovaya/',
 '/catalog/frukty-i-ovoshchi-rezannye-chishchennye/',
 '/catalog/frukty-ovoshchi-zelen-2/',
 '/catalog/frukty/',
 '/catalog/gaspacho-so-strachatelloy/',
 '/catalog/gazirovannye-napitki/',
 '/catalog/gel-dlya-ruk-1/',
 '/catalog/gel-dlya-ruk/',
 '/catalog/gigiena-ukhod/',
 '/catalog/gotovye-blyuda-dlya-prazdnika/',
 '/catalog/gotovye-zavtraki-myusli/',
 '/catalog/gribnaya-1/',
 '/catalog/gribnaya/',
 '/catalog/griby-1/',
 '/catalog/griby/',
 '/catalog/gril-barbekyu/',
 '/catalog/grusha-s-krevetkami/',
 '/catalog/grushevyy-pirog/',
 '/catalog/idei-dlya-podarkov/',
 '/catalog/igrushki-1/',
 '/catalog/igrushki-aksessuary/',
 '/catalog/igrushki/',
 '/catalog/ikra-2022-1/',
 '/catalog/ikra-2022/',
 '/catalog/ikra-2023/',
 '/catalog/ikra/',
 '/catalog/iqos-zazhigalki-spichki-aksessuary/',
 '/catalog/iqos/',
 '/catalog/italyanskiy-salat/',
 '/catalog/iz-kozego-moloka/',
 '/catalog/izdeliya-iz-ryby-i-moreproduktov/',
 '/catalog/kakao-shokolad/',
 '/catalog/karamel-ledentsy-drazhe-/',
 '/catalog/kashi-gotovye-zavtraki/',
 '/catalog/kashi/',
 '/catalog/kaurdak/',
 '/catalog/ketchupy-i-sousy/',
 '/catalog/khleb-bagety-tandyr/',
 '/catalog/khleb-khlebtsy/',
 '/catalog/khleb-lavash-lepeshki/',
 '/catalog/khleb-torty-sladosti-1/',
 '/catalog/kholodnyy-chay/',
 '/catalog/khot-dog/',
 '/catalog/kislomolochnye-produkty-zakvaska/',
 '/catalog/klern-1/',
 '/catalog/klern-2/',
 '/catalog/klern-3/',
 '/catalog/kofe-i-chay/',
 '/catalog/kofe-tsikoriy/',
 '/catalog/kofe-v-kapsulakh/',
 '/catalog/kolbasnye-i-myasnye-narezki/',
 '/catalog/kolbasy-i-sosiski/',
 '/catalog/kolbasy-sosiski-myasnye-delikatesy/',
 '/catalog/kolbasy-vetchina-1/',
 '/catalog/komnatnye-tsvety-1/',
 '/catalog/komnatnye-tsvety-2/',
 '/catalog/komnatnye-tsvety/',
 '/catalog/konditerskie-izdeliya-2/',
 '/catalog/konfety-podarochnye-nabory-1/',
 '/catalog/konfety-shokolad-sladosti/',
 '/catalog/konservatsiya/',
 '/catalog/konservy-orekhi-sneki-varene/',
 '/catalog/konyaki-i-konyachnye-napitki/',
 '/catalog/kopchyenaya-i-vyalenaya-ryba/',
 '/catalog/korma-dlya-zhivotnykh-1/',
 '/catalog/kotlety/',
 '/catalog/krasota-gigiena-zdorove-1/',
 '/catalog/krem-sup-iz-zapechennykh-ovoshchey/',
 '/catalog/krupy-1/',
 '/catalog/krupy/',
 '/catalog/kukhnya-ot-spar-2/',
 '/catalog/kulich-mon-chouchou/',
 '/catalog/kulinariya-dlya-detey-1/',
 '/catalog/kulinariya-dlya-detey/',
 '/catalog/kurinye-krylya/',
 '/catalog/kvas-kvasnye-napitki/',
 '/catalog/la-florentina-iz-italii-1/',
 '/catalog/la-florentina-iz-italii/',
 '/catalog/lanchboksy-konteynery/',
 '/catalog/lazanya/',
 '/catalog/lepim-varim-zamorozhennye/',
 '/catalog/lichnaya-gigiena/',
 '/catalog/lumakoni/',
 '/catalog/maffiny-pechene-biskvity/',
 '/catalog/makarony-1/',
 '/catalog/makarony-krupy-maslo-konservatsiya/',
 '/catalog/makarony-krupy-spetsii-maslo-1/',
 '/catalog/makarony-krupy-sukhie-zavtraki/',
 '/catalog/makarony-krupy/',
 '/catalog/makarony/',
 '/catalog/mandarinovye-kapkeyki/',
 '/catalog/marmelad-sparkie-1/',
 '/catalog/marmelad-sparkie/',
 '/catalog/martini-vermuty-aperitivy/',
 '/catalog/maski-i-perchatki--1/',
 '/catalog/maski-i-perchatki-/',
 '/catalog/masla-i-uksus/',
 '/catalog/masla-uksus-1/',
 '/catalog/masla-uksus/',
 '/catalog/masla/',
 '/catalog/maslo-margarin/',
 '/catalog/mayonez-1/',
 '/catalog/mayonez/',
 '/catalog/megaskidki-2/',
 '/catalog/melochi-vozle-kass/',
 '/catalog/midii-v-souse/',
 '/catalog/molochnaya-produktsiya/',
 '/catalog/molochnaya/',
 '/catalog/molochnye-deserty/',
 '/catalog/molochnye-i-rastitelnye-napitki-1/',
 '/catalog/molochnye-i-rastitelnye-napitki/',
 '/catalog/molochnye-produkty-i-moloko/',
 '/catalog/molochnye-produkty/',
 '/catalog/moloko-syr-yaytsa-1/',
 '/catalog/moloko/',
 '/catalog/moreprodukty-krevetki-1/',
 '/catalog/moreprodukty-krevetki-2/',
 '/catalog/moreprodukty-krevetki/',
 '/catalog/morozhenoe-2/',
 '/catalog/morozhenoe/',
 '/catalog/morsy-uzvary-kompoty-kiseli/',
 '/catalog/muchnye-izdeliya/',
 '/catalog/muka-tovary-dlya-vypechki/',
 '/catalog/musaka/',
 '/catalog/muzhskaya-gigiena/',
 '/catalog/myasnaya-kolbasnaya-rybnaya-gastronomiya/',
 '/catalog/myasnaya/',
 '/catalog/myasnye-delikatesy-1/',
 '/catalog/myasnye-fermerskie-produkty-1/',
 '/catalog/myasnye-fermerskie-produkty/',
 '/catalog/myaso-kraba/',
 '/catalog/myaso-ptitsa-kolbasy-1/',
 '/catalog/myaso/',
 '/catalog/mylo/',
 '/catalog/naggetsy/',
 '/catalog/napitki-4/',
 '/catalog/napitki-bezalkogolnye-1/',
 '/catalog/napitki-i-deserty/',
 '/catalog/napitki-spar/',
 '/catalog/nashi-marki/',
 '/catalog/naushniki-zaryadnye-ustroystva-/',
 '/catalog/noski-kolgotki-golfy/',
 '/catalog/noski-kolgotki-obuv-1/',
 '/catalog/novinki-2/',
 '/catalog/novinki-spar/',
 '/catalog/novinki/',
 '/catalog/novyy-ulov/',
 '/catalog/obedy-s-11-do-18/',
 '/catalog/obuv/',
 '/catalog/obuvnaya-kosmetika-i-aksessuary/',
 '/catalog/obuvnaya-kosmetika-i-akssesuary/',
 '/catalog/ochishchennye-rezanye-varyenye/',
 '/catalog/odezhda-obuv-khranenie-ukhod/',
 '/catalog/odnorazovaya-posuda/',
 '/catalog/okhlazhdennaya-ryba-2022/',
 '/catalog/okhlazhdennaya-ryba-i-myaso/',
 '/catalog/okhlazhdennaya-ryba/',
 '/catalog/okhlazhdennoe-i-zamorozhennoe/',
 '/catalog/okhlazhdennye-i-zamorozhennye-polufabrikaty/',
 '/catalog/olivki-i-masliny-1/',
 '/catalog/olivki-i-masliny/',
 '/catalog/olivki-los-curado/',
 '/catalog/omlet-pulyar/',
 '/catalog/orekhi-i-sukhofrukty-1/',
 '/catalog/orekhi-sukhofrukty-semechki-2/',
 '/catalog/orekhi-sukhofrukty-semechki-3/',
 '/catalog/orekhi-sukhofrukty-semechki-4/',
 '/catalog/orekhi-sukhofrukty-semechki/',
 '/catalog/osobaya-kollektsiya-molochnaya-1/',
 '/catalog/osobaya-kollektsiya-morozhenoe/',
 '/catalog/osobaya-kollektsiya-myasnaya/',
 '/catalog/osvezhayushchie-kokteyli/',
 '/catalog/osvezhiteli-vozdukha-1/',
 '/catalog/osvezhiteli-vozdukha/',
 '/catalog/ovoshchi-frukty-yagody-griby-1/',
 '/catalog/ovoshchi/',
 '/catalog/ovoshchnaya-konservatsiya-1/',
 '/catalog/ovoshchnaya/',
 '/catalog/paelya/',
 '/catalog/pankeyki-s-golubikoy/',
 '/catalog/pashtety-1/',
 '/catalog/pechene-vafli-pryaniki-1/',
 '/catalog/pechene-vafli-pryaniki/',
 '/catalog/pekarnya-spar/',
 '/catalog/pelmeni/',
 '/catalog/pirog-s-motsarelloy/',
 '/catalog/pirogi-bulochki-keksy-rulety/',
 '/catalog/pirogi-bulochki-sloyki/',
 '/catalog/pirogi-khleb-tartaletki/',
 '/catalog/pitstsa-2/',
 '/catalog/pitstsa-burgery-shaurma-2/',
 '/catalog/pitstsa-burgery-shaurma/',
 '/catalog/pitstsa/',
 '/catalog/pivo-1/',
 '/catalog/pivo-i-bezalkogolnoe-vino/',
 '/catalog/podarki-dlya-malenkikh-ledi/',
 '/catalog/podarochnaya-upakovka-1/',
 '/catalog/podarochnaya-upakovka/',
 '/catalog/podarochnye-nabory-1/',
 '/catalog/podarochnye-nabory-2/',
 '/catalog/podarochnye-nabory-chaya/',
 '/catalog/podarochnye-nabory-konfet-2/',
 '/catalog/podarochnye-nabory-konfet-4/',
 '/catalog/podarochnye-nabory/',
 '/catalog/podguzniki/',
 '/catalog/poke-iz-lososya/',
 '/catalog/poleznye-napitki/',
 '/catalog/poleznye-produkty/',
 '/catalog/poleznye-sladosti/',
 '/catalog/polufabrikaty-1/',
 '/catalog/polufabrikaty-iz-ryby-i-moreproduktov/',
 '/catalog/polufabrikaty-po-retseptu-spar/',
 '/catalog/postnoe-menyu-/',
 '/catalog/postnoe-menyu/',
 '/catalog/posuda-gustex-1/',
 '/catalog/posuda-gustex-2/',
 '/catalog/posuda-gustex/',
 '/catalog/premialnye-syry/',
 '/catalog/preservy-iz-ulova-2022/',
 '/catalog/prezervativy-lubrikanty-testy-1/',
 '/catalog/prezervativy-lubrikanty-testy/',
 '/catalog/produkty-bez-glyuteina/',
 '/catalog/produkty-bystrogo-prigotovleniya/',
 '/catalog/proteinovye-batonchiki/',
 '/catalog/ptitsa/',
 '/catalog/purina-one/',
 '/catalog/pyure/',
 '/catalog/rassada-zelen-1/',
 '/catalog/rassada-zelen/',
 '/catalog/rastitelnye-molochnye-produkty/',
 '/catalog/rastitelnye-produkty-1/',
 '/catalog/ratatuy/',
 '/catalog/retsepty/',
 '/catalog/rizotto/',
 '/catalog/roliki-dlya-odezhdy-1/',
 '/catalog/roliki-dlya-odezhdy-2/',
 '/catalog/roliki-dlya-odezhdy/',
 '/catalog/rom-tekila-dzhin-absent/',
 '/catalog/royal-barber-1/',
 '/catalog/royal-barber-2/',
 '/catalog/ryba-i-moreprodukty-v-individualnoy-upakovke/',
 '/catalog/ryba-moreprodukty-ikra/',
 '/catalog/ryba-v-individualnoy-upakovke/',
 '/catalog/ryba/',
 '/catalog/rybnaya-1/',
 '/catalog/rybnaya/',
 '/catalog/rybnoe-delo/',
 '/catalog/rybnye-delikatesy/',
 '/catalog/rybnye-kotlety/',
 '/catalog/s-pylu-s-zharu/',
 '/catalog/sakhar/',
 '/catalog/sakharozameniteli/',
 '/catalog/salat-iz-mandarinov/',
 '/catalog/salat-s-mango-i-krevetkami/',
 '/catalog/salaty-sousy/',
 '/catalog/sendvichi-1/',
 '/catalog/sgushchennoe-moloko/',
 '/catalog/shampanskoe-igristye-vina/',
 '/catalog/shashlyk/',
 '/catalog/sheykery-i-butylki/',
 '/catalog/shokolad-jacques/',
 '/catalog/shokolad-shokoladnye-batonchiki-2/',
 '/catalog/shokoladnaya-arakhisovaya-pasta-1/',
 '/catalog/shokoladnye-batonchiki/',
 '/catalog/shokoladnye-konfety-/',
 '/catalog/shokoladnye-konfety-iz-italii/',
 '/catalog/shokoladnyy-keks/',
 '/catalog/skoro-novyy-god/',
 '/catalog/slaboalkogolnye-napitki/',
 '/catalog/sladkaya-konservatsiya/',
 '/catalog/sladkie-podarki-1/',
 '/catalog/sladkie-podarki-2/',
 '/catalog/sladkie-sneki/',
 '/catalog/sladosti-1/',
 '/catalog/sladosti-i-svitboksy-1/',
 '/catalog/sladosti-i-svitboksy-2/',
 '/catalog/sladosti-i-svitboksy-3/',
 '/catalog/sladosti-i-svitboksy-5/',
 '/catalog/sladosti-i-svitboksy/',
 '/catalog/sladosti-vypechka-pechene/',
 '/catalog/slivki/',
 '/catalog/smart/fasol-smart-struchkovaya-rezanaya-400g/',
 '/catalog/smart/kapusta-tsvetnaya-smart-400g/',
 '/catalog/smart/klubnika-smart-300g/',
 '/catalog/smart/klyukva-sadovaya-smart-300g/',
 '/catalog/smart/shampinony-smart-rezanye-400g/',
 '/catalog/smart/smes-ovoshchnaya-smart-gavayskaya-400g/',
 '/catalog/smart/smes-ovoshchnaya-smart-letnyaya-400g/',
 '/catalog/smart/smes-ovoshchnaya-smart-meksikanskaya-400g/',
 '/catalog/smart/vishnya-smart-bez-kostochki-300g/',
 '/catalog/smetana/',
 '/catalog/smuzi-boul/',
 '/catalog/smuzi-sokosoderzhashchie-napitki/',
 '/catalog/sneki-1/',
 '/catalog/sneki-2/',
 '/catalog/sneki-iz-ryby-i-moreproduktov/',
 '/catalog/sneki-orekhi-sukhofrukty-pravilnoe-pitanie/',
 '/catalog/soki-nektary/',
 '/catalog/sol-sakhar-muka-spetsii/',
 '/catalog/sol-sakhar-spetsii-pripravy/',
 '/catalog/solenaya-i-kopchenaya-ryba-1/',
 '/catalog/solenaya-i-kopchenaya-ryba/',
 '/catalog/soleniya-koreyskie-salaty-2/',
 '/catalog/soleniya-koreyskie-salaty/',
 '/catalog/soleniya/',
 '/catalog/solyenaya-ryba/',
 '/catalog/sosiski-sardelki-shpikachki-1/',
 '/catalog/sousy-ketchupy/',
 '/catalog/spagetti-s-frikadelkami/',
 '/catalog/spar/brusnika-spar-300g/',
 '/catalog/spar/grib-belyy-rezannyy-spar-300g/',
 '/catalog/spar/kapusta-bryusselskaya-spar-400g/',
 '/catalog/spar/kartofel-fri-spar-400g/',
 '/catalog/spar/kartofelnye-dolki-spar-300g/',
 '/catalog/spar/malina-spar-300g/',
 '/catalog/spar/oblepikha-spar-300g/',
 '/catalog/spar/smes-italyanskaya-spar-400g/',
 '/catalog/spar/smes-spar-ovoshchi-dlya-zharki-400g/',
 '/catalog/spar/smes-tsvetnaya-kapusta-i-brokkoli-spar-400g/',
 '/catalog/sparzha-s-file-treski/',
 '/catalog/spichki-zazhigalki-1/',
 '/catalog/sportivnoe-pitanie-1/',
 '/catalog/sportivnoe-pitanie/',
 '/catalog/sredstva-dlya-britya-i-depilyatsii/',
 '/catalog/sredstva-dlya-britya/',
 '/catalog/sredstva-dlya-uborki/',
 '/catalog/sredstva-ot-nasekomykh-1/',
 '/catalog/sredstva-ot-nasekomykh/',
 '/catalog/steyk-iz-file-utki/',
 '/catalog/steyki-dlya-grilya-1/',
 '/catalog/sukhari-baranki-sushki/',
 '/catalog/sukhariki/',
 '/catalog/sukhie-smesi-zameniteli-moloka/',
 '/catalog/sumki-zonty-perchatki-1/',
 '/catalog/sumki-zonty-perchatki/',
 '/catalog/sup-ramen/',
 '/catalog/superfudy-1/',
 '/catalog/superfudy/',
 '/catalog/supy/',
 '/catalog/sushi-rolly/',
 '/catalog/syrniki-iz-rikotty/',
 '/catalog/syrnoe-morozhenoe/',
 '/catalog/syrnye-narezki/',
 '/catalog/syrovyalenye-i-syrokopchenye-kolbasy/',
 '/catalog/syry/',
 '/catalog/tako/',
 '/catalog/tekstil/',
 '/catalog/teplyy-salat/',
 '/catalog/testo-1/',
 '/catalog/testo/',
 '/catalog/torty-bocconto-1/',
 '/catalog/torty-bocconto-3/',
 '/catalog/torty-bocconto/',
 '/catalog/torty-pirozhnye-deserty-1/',
 '/catalog/torty-pirozhnye-korzhi-tartaletki/',
 '/catalog/torty-pirozhnye-ponchiki/',
 '/catalog/torty-pirozhnye-ponchiki/f/type-is-pirozhnye/',
 '/catalog/torty-pirozhnye-ponchiki/f/type-is-torty/',
 '/catalog/tovary-dlya-detey-1/',
 '/catalog/tovary-dlya-doma-i-otdykha/',
 '/catalog/tovary-dlya-doma/',
 '/catalog/tovary-dlya-prazdnika-1/',
 '/catalog/tovary-dlya-prazdnika-2/',
 '/catalog/tovary-dlya-prazdnika-i-kantstovary-1/',
 '/catalog/tovary-dlya-shkoly/',
 '/catalog/tovary-dlya-uborki/',
 '/catalog/tovary-dlya-zhivotnykh-2/',
 '/catalog/tovary-dlya-zhivotnykh/',
 '/catalog/travyanoy-chay/',
 '/catalog/tsvety-3/',
 '/catalog/tsvety-4/',
 '/catalog/tsvety-otkrytki-prazdnik/',
 '/catalog/tualetnaya-bumaga/',
 '/catalog/tvorog-syrki-tvorozhnye-produkty/',
 '/catalog/tykvennye-bulochki/',
 '/catalog/tykvennyy-krem-sup/',
 '/catalog/tykvennyy-pirog/',
 '/catalog/udobreniya-grunt-inventar-1/',
 '/catalog/udobreniya-grunt-inventar/',
 '/catalog/ugol-mangal-rozzhig/',
 '/catalog/ukhod-za-litsom/',
 '/catalog/ukhod-za-polostyu-rta/',
 '/catalog/ukhod-za-telom/',
 '/catalog/ukhod-za-volosami/',
 '/catalog/ukrasheniya/',
 '/catalog/ustroystva-lil/',
 '/catalog/utka/',
 '/catalog/uzhiny-s-18-do-21/',
 '/catalog/varene-med-sirop-2/',
 '/catalog/varene-med-sirop-3/',
 '/catalog/varene-med-sirop/',
 '/catalog/vareniki-1/',
 '/catalog/vazy-gorshki-dlya-tsvetov-1/',
 '/catalog/vazy-gorshki-dlya-tsvetov-2/',
 '/catalog/vegetarianskaya-okroshka/',
 '/catalog/vegetarianskie-kolbasy-i-pashtety-1/',
 '/catalog/vegetarianskie-kolbasy-i-pashtety/',
 '/catalog/vegetarianskiy-karri/',
 '/catalog/vesovye-konfety/',
 '/catalog/vino/',
 '/catalog/viski-brendi/',
 '/catalog/vitaminy-i-biologicheski-aktivnye-dobavki/',
 '/catalog/vkusno-ot-laurieri/',
 '/catalog/vlazhnye-salfetki-1/',
 '/catalog/vlazhnye-salfetki/',
 '/catalog/voda-1/',
 '/catalog/voda-napitki-chay/',
 '/catalog/voda-soki-napitki-1/',
 '/catalog/voda-soki-napitki/',
 '/catalog/voda/',
 '/catalog/vodka-nastoyki/',
 '/catalog/vostochnye-sladosti-1/',
 '/catalog/vtorye-blyuda/',
 '/catalog/yagody-frukty-ovoshchi-1/',
 '/catalog/yagody/',
 '/catalog/yaytso/',
 '/catalog/yogurty/',
 '/catalog/zakuski-goryachie-kholodnye-1/',
 '/catalog/zamorozhennaya-ryba-2022/',
 '/catalog/zamorozhennaya-ryba-2023/',
 '/catalog/zamorozhennaya-ryba/',
 '/catalog/zamorozhennoe-myaso-i-ryba/',
 '/catalog/zamorozhennye-ovoshchi-yagody-griby-1/',
 '/catalog/zamorozhennye-ovoshchi-yagody-griby-2/',
 '/catalog/zamorozhennye-ovoshchi-yagody-griby/',
 '/catalog/zamorozhennye-produkty-2/',
 '/catalog/zamorozhennye-vtorye-blyuda/',
 '/catalog/zapechennaya-tykva/',
 '/catalog/zapechyennaya-forel/',
 '/catalog/zapekanka-iz-pelmeney/',
 '/catalog/zavtraki-1/',
 '/catalog/zdorovoe-pitanie/',
 '/catalog/zdorovyy-perekus/',
 '/catalog/zefir-marmelad-pastila-1/',
 '/catalog/zelen-salaty-2/',
 '/catalog/zelen-salaty/',
 '/catalog/zharenye-krevetki/',
 '/catalog/zharenyy-lagman/',
 '/catalog/zhenskaya-gigiena/',
 '/catalog/zhevatelnaya-rezinka-ledentsy-1/',
 '/catalog/zhevatelnaya-rezinka-ledentsy-2/',
 '/catalog/zhevatelnye-konfety-iris/',
        ]
        
        
    #url = "https://myspar.ru/catalog/zhevatelnye-konfety-iris/"
    #req = Request(url)
    #req.add_header('Accept', '__text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
    #req.add_header('Accept-Encoding', 'gzip, deflate, br')
    #req.add_header('Accept-Language', 'ru-RU,ru;q=0.9')
    #req.add_header('Cache-Control', 'no-cache')
    #req.add_header('Connection', 'keep-alive')
    #req.add_header('Host', 'myspar.ru')
    #req.add_header('Pragma', 'no-cache')
    #req.add_header('sec-ch-ua', '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"')
    ##req.add_header('sec-ch-ua-mobile:', '?0')
    #req.add_header('sec-ch-ua-platform', '"macOS"')
    #req.add_header('Sec-Fetch-Dest', 'document')
    #req.add_header('Sec-Fetch-Mode', 'navigate')
    #req.add_header('Sec-Fetch-Site', 'none')
    #req.add_header('Sec-Fetch-User', '?1')
    #req.add_header('Upgrade-Insecure-Requests', '1')
    #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) #Chrome/98.0.4758.109 Safari/537.36')
    #content = urlopen(req).read()
    #print(content)


    def process(self):
        self.__list_dict = []
        for url in self.__urls:
            url = 'https://myspar.ru' + url + '?sort=price-asc'
            for i in range(1,6):
                url_r = url + '&PAGEN_1=' + str(i)
                for object_params in ListPage(url_r).list_dict():
                    self.__list_dict.append(object_params)

    def __create_file_name_with_current_datetime(self):
        return 'spar_fresh.json'

    def save_in_file_with_current_datetime(self):
        json_string = json.dumps(self.__list_dict)
        file_name = self.__create_file_name_with_current_datetime()
        with open(file_name, 'w') as outfile:
            json.dump(json_string, outfile)

    def send_in_api(self):
        configuration = openapi_client.Configuration(
            host = "http://absrent.ru:8000"
        )

        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = history_api.HistoryApi(api_client)
            for e in self.__list_dict:
                #print(e)
                history = History(
                    pk=1,
                    title=e['title'],
                    quantity=1,
                    price=str(e['price']),
                    price_sale=str(e['price_sale']),
                    datetime_create="1970-01-01T00:00:00.00Z",
                    #score="-807",
                    #count_comments=1,
                    #count_likes=1,
                    #count_stars_all=1,
                    #count_stars_1=1,
                    #count_stars_2=1,
                    #count_stars_3=1,
                    #count_stars_4=1,
                    #count_stars_5=1,
                    #count_how_much_buy=1,
                    #count_questions=1,
                    #count_photo=1,
                    #category="category_example",
                    #category_url="category_url_example",
#                    brand=e["brand"],
#                    brand_url=e["brand_url"],
                    #day_to_delivery=1,
                    #sku="sku_example",
                    url=e['url'],
                    #canonical_url="canonical_url_example",
#                    img_url=e["image_url"],
                    #description="description_example",
                    #params="params_example",
                    #seller="seller_example",
                    #seller_url="seller_url_example",
                    source_url=e["source_url"],
                    #urls_other_products_on_the_page="urls_other_products_on_the_page_example",
                    #worker="worker_example",
                    #task="task_example",
                ) # History |  (optional)

                try:
                    api_response = api_instance.history_create(body=history)
                    #pprint(api_response)
                except openapi_client.ApiException as e:
                    print("Exception when calling HistoryApi->history_create: %s\n" % e)
            print('Count load object =', len(self.__list_dict))