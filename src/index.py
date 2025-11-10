from varasto import Varasto


def lisaa_mehu_varastoon(mehua, maara):
    print(f"Mehuvarasto: {mehua}")
    print(f"Lisätään {maara}")
    mehua.lisaa_varastoon(maara)
    print(f"Mehuvarasto: {mehua}")


def ota_mehu_varastosta(mehua, maara):
    print(f"Mehuvarasto: {mehua}")
    print(f"Otetaan {maara}")
    saatiin = mehua.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def lisaa_olut_varastoon(olutta, maara):
    print(f"Olutvarasto: {olutta}")
    print(f"Lisätään {maara}")
    olutta.lisaa_varastoon(maara)
    print(f"Olutvarasto: {olutta}")


def ota_olut_varastosta(olutta, maara):
    print(f"Olutvarasto: {olutta}")
    print(f"Otetaan {maara}")
    saatiin = olutta.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def tulosta_varastotilanne(mehua, olutta):
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulosta_varastotilanne(mehua, olutta)

    olut_getterit(olutta)

    lisaa_olut_varastoon(olutta, 1000.0)
    lisaa_mehu_varastoon(mehua, -666.0)
    ota_olut_varastosta(olutta, 1000.0)
    ota_mehu_varastosta(mehua, -32.9)


if __name__ == "__main__":
    main()
