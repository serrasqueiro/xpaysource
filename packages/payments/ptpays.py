# -*- coding: iso-8859-1 -*-
# ptpays.py  (c)2021  Henrique Moreira

"""
Miscelaneous payment methods
"""

# pylint: disable=line-too-long


METHODS_2021 = {	# Usual description in debt: company-key
    "DDPT16103627": "FitnessHut",
    "ENT:21159": "MEO",	# "PAG.SERVICOS ENT:21159 REF:nnn"
    "ENT:21604": "EUPAGO",	# either "PAG.SERVICOS ENT:21604" or "PAG SERV 21604/nnn EUPAGO"
    "21604": "EUPAGO",	# (see "ENT:21604")
    "10611": "EASYPAY",	# e.g. "PAG SERV 10611/nnn EASYPAY INSTITUICAO DE" (caridade)
    "11589": "WORTEN",	# e.g. "PAG COMP 11589/nnn WORTEN ..."
    "10155": "LDC",	# "LOJA DO CONDOMINIO"
    "PAG.D.G.T": "Imposto",	# pagamento � Dire��o Geral do Tesouro
    "LU96000000": "Paypal",	# e.g. DD LU96000000 PAYPAL (EUROPE) <ref>
    }

METHOD_BY_DATE = {
    "FitnessHut": (
        {"from": None, "to": None, "list": None,},
        )
    }


INFO_CONTEXTS = {
    "EASYPAY": (
        "$1 EASYPAY",
        "* $2/ EASYPAY", # PAG.SERV
        ),
    "EUPAGO": (
        "* $2/ EUPAGO",
        ),
    "MEO": (
        "PAG.SERVICOS $2",	# e.g. "PAG.SERVICOS ENT:21159" ...
        ),
    "WORTEN": (
        "* * $3/ WORTEN",
        ),
    "LOJA DO CONDOMINIO": (
        "* * $3/ LOJA",
        ),
    "DGT": (
        "PAG.D.G.T *",
        ),
    "PAYPAL": (
        "* $2 PAYPAL",
        ),
    }

URL_CONTEXTS = {
    "EASYPAY": (
        "https://www.easypay.pt/pt/easypay-extrato-bancario",
    ),
    "EUPAGO": (
        "https://www.eupago.pt/",
    ),
    "MEO": (
        "https://www.meo.pt/",
    ),
    "WORTEN": (
        "https://www.worten.pt/",
    ),
}

INFO_COMPANIES = {
    "FitnessHut": {
        "abbrev": "gymn",
        "url-sample": "https://www.fitnesshut.pt/",
        }
    }


# Notes:
# - Not a complete list of 'Entidade' (MB in Portugal)
#
#	EasyPay -> Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares
#	10061  NOS COMUNICACOES SA
#	10074  Carregamento telem�vel operadora (??)
#	10081  OTLIS Operadores de Transportes Regi�o de Lisboa ACE
#	10083  TIP-TRANSPORTES INTERMODAIS PORTO ACE
#	10095  Pagamentos ao Estado
#	10121  ACP (Autom�vel Clube de Portugal)
#	10126  Seguradoras Unidas SA
#	10128  FIDELIDADE COMPANHIA SEGUROS SA
#	10130  EDEN SPRINGS Portugal SA
#	10131  TRANSPORTES AEREOS PORTUGUESES
#	10132  Liberty Seguros
#	10155  LOJA DO CONDOMINIO
#	10158  VODAFONE PORTUGAL COMUNICACOES PESSOAIS
#	10175  Sele��es Readears Digest
#	10196  FAGAR  FARO, GEST�O DE �GUAS E RES�DUOS
#	10208  Global Noticias  An�ncios Jornal de Noticias
#	10211  C�mara Municipal do Porto
#	10212  MOTOR PRESS LISBOA,EDICAO E DISTRIB. SA
#	10227  CARAVELA-COMPANHIA DE SEGUROS SA
#	10231  INATEL
#	10241  CompraFacil (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares. (*)
#	10244  Victoria Seguros
#	10261  OK TeleSeguro
#	10277  NOS COMUNICACOES SA
#	10294  AGEAS PORTUGAL COMPANHIA SEGUROS SA
#	10297  Vodafone Portugal
#	10311  ORDEM DOS Engenheiros
#	10314  Instituto Politecnico Viana Do Castelo
#	10335  ORDEM DOS Enfermeiros
#	10351  NOS Madeira Comunica��es
#	10363  FNAC
#	10377  MAPFRE SEGUROS GERAIS, S.A.
#	10404  COOPERATIVA FORMACAO ANIMACAO CULTURAL
#	10411  CERTIEL-ASSOC.CERTIFICADORA INST.ELECT.
#	10420  FIDELIDADE COMPANHIA SEGUROS SA
#	10422  INCM
#	10451  ISEP  Instituto Superior de Engenharia do Porto
#	10455  LIBERTY SEGUROS SA
#	10482  F.C. Porto Pagamento quotas de s�cio  Sportinveste Multimedia SA
#	10511  Porto Editora  Escola Virtual
#	10550  OTIS ELEVADORES LDA
#	10559  Ifthenpay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	10565  Intrum Justitia (Presta servi�os a empresas, ex.: EDP)
#	10575  VIAGENS ABREU SA
#	10611  EasyPay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares. (*)
#	10612  SWEETS 4 U  COM. E REP.PROD.ALIM.LDA
#	10641  INST.GEST.FINAC INFRA ESTRU JUSTICA IP
#	10644  Toconline  Licensa de utiliza��o de programa de factura��o
#	10652  SAGE Portugal
#	10828  NESTLE PORTUGAL SA
#	10941  IGCP  Ag�ncia de Gest�o e da Tesousaria e da D�vida P�blica
#	10950  Instituto da Vinha e do Vinho
#	10954  MEO
#	10958  ISEP  Instituto Superior de Engenharia do Porto
#	10982  Armaz�ns Marques Soares
#	10991  STAPLES Portugal SA
#	10996  ADENE Ag�ncia para a Energia
#	---
#	11012  Instituto Registos e Notariado,IP
#	11013  Portal da Empresa
#	11017  Via directa, companhia de seguros SA
#	11024  Lusopay  Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares.
#	11034  FIDELIDADE COMPANHIA SEGUROS SA
#	11056  NSeguros
#	11062  A.C.P. MEDIACAO SEGUROS SA
#	11063  SEGURADORAS UNIDAS, SA
#	11089  CGA  Caixa Geral de Aposenta��es
#	11100  CLINICA CUF CASCAIS, S.A.
#	11163  VILLAS BOAS ACP  ARCHER CAMACHO
#	11175  Instituto M�dico Scalabitano
#	11202  Ifthenpay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	11206  AGENCIA PARA MODERNIZACAO ADMINISTRATIVA
#	11216  MUNICIPIO DE ESTREMOZ
#	11241  La Redoute
#	11249  CompraFacil (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas/ particulares, Conforama, HiMedia, Lap2Go.pt, Globalsport.pt, Mister Auto, Betfair (*), ou HIPAY.COM
#	11283  EDP
#	11286  HOSPITAL DA LUZ SA
#	11299  Pagamento IES  Informa��o Empresarial Simplificada
#	11302  Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares.
#	11314  ONSALESIT SA
#	11335  ????
#	11341  SAMS Quadros
#	11360  Hospital CUF Porto
#	11364  Endesa
#	11369  Empark Portugal-Empreendimentos e Explora��o de Parqueamentos
#	11390  2B STYLE UNIPESSOAL LDA
#	11409  COURLUX INTERNATIONAL
#	11412  Pagamento de an�ncios Standvirtual / Imovirtual
#	11413  TAP
#	11419  OPENSOFT SOLUCOES INFORMATICAS SA
#	11421  CAMARA MUNICIPAL DE LISBOA
#	11440  ISEP Carregamento Cart�o Alimenta��o
#	11454  DIRECCAO GERAL ADMNISTRACAO JUSTICA
#	11456  GOLD ENERGY-COMERCIALIZADORA ENERGIA SA
#	11471  TRANSPORTES AEREOS PORTUGUESES
#	11473  Ifthenpay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares) / Cl�nica Paris
#	11496  UNIVERSIDADE DO PORTO
#	11583  Gas Natural Servi�os SDG SA
#	11589  Worten
#	11604, 11686, 11687, 11802, 11873, 11925, 11988, 11989, 11990  Ifthenpay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	11606  CIF-AGENCIA DE VIAGENS E TURISMO, SA
#	11609  INST SUP CIENCIAS SOCIAIS POLITICAS
#	11644  IBERDROLA ENERGIA
#	11663  Municipio de Santo Tirso
#	11669  MULTICERT
#	11672  Noticias Direct Distribui��o Ao Domicilio Lda
#	11683  EASYPAY Institui��o de pagamentos LDA
#	11687  Audilar  R�dio Popular
#	11693  CENTRO HOSPITALAR E UNIVERSITARIO DE COIMBRA
#	11706  UNIVERSIDADE LISBOA  Ver�o na Ulisboa
#	11708  MHR ou PT PAY SA
#	11711  INSTITUTO REGISTOS NOTARIADO,IP
#	11712  INSTITUTO REGISTOS NOTARIADO,IP
#	11713  INSTITUTO REGISTOS NOTARIADO,IP
#	11714  INSTITUTO REGISTOS NOTARIADO,IP
#	11717  INST. EMP. FORM. PROFISSIONAL (IEFP)
#	11726  VERTBAUDET PORTUGAL LDA
#	11733  AlmourolTec / PTisp
#	11737  Ticket Restaurant
#	11749  Sport Zone
#	11758  SATA Internacional
#	11767  Comiss�o de Viticultura da Regi�o Vinhos Verdes
#	11768  MUNICIPIO DE VIANA DO CASTELO
#	11782  EASYPAY INSTITUICAO DE PAGAMENTOS LDA
#	11795  Instituto dos Registos e do Notariado  Registo Predial Online, RPO
#	11802  ifthenpay
#	11811  CENTRO SOCIAL DA LEGIAO DA BOA VONTADE
#	11843  EASYPAY INSTITUICAO DE PAGAMENTOS LDA
#	11846  IBERDROLA ENERGIA
#	11854  PPRO FINANCIAL LTD  Entidade de servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares. (*)
#	11873  IFTHENPAY LDA
#	11877  EUPAGO INSTITUICAO PAGAMENTO LDA / Pagmento programa factura��o Invoice Express
#	11893  HPME SA  HI-MEDIA PORTE MONNAIE �LECTRONIQUE (HPME) SA  Entidade que faculta servi�os de pagamento a terceiros
#	11896  INSTITUTO DE AVALIACAO EDUCATIVA
#	11911  C�mara Municipal de Ovar
#	11916  VIA VERDE PORTUGAL-S.G.E.COBRANCAS SA
#	11921  Vit�ria Seguros, S.A
#	11925  IFTHENPAY LDA
#	11937  Instituto dos Registos e do Notariado
#	11944  Brisa / Via verde
#	11950  CAMARA MUNICIPAL DE LISBOA
#	11967  IFTHENPAY LDA (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	11976  Munic�pio de Santa Maria da Feira
#	11979  PAYPAYUE I PAG UNIP LDA
#	11985  GALP Power, SA
#	11988  ifthenpay (Audilar, Delikatessen, etc)
#	11989  ifthenpay (pequenas empresas e particulares)
#	11990  ifthenpay (Aqu�rio)
#	11999  EPorto, Estacionamentos P�blicos do Porto (multas estacionamento)
#	---
#	12009  GOLD ENERGY
#	12020  EASYPAY INSTITUICAO DE PAGAMENTOS LDA
#	12029  HPME SA  HI-MEDIA PORTE MONNAIE �LECTRONIQUE (HPME) SA  Entidade que faculta servi�os de pagamento a terceiros. (*)
#	12057  DALENYS PAYMENT
#	12061  EL CORTE INGLES GRANDES ARMAZENS SA
#	12121  ENDESA ENERGIA SUCURSAL PORTUGAL
#	12132  Metro do Porto
#	12133  ifthenpay (CDUP)
#	12142  EUPAGO INSTITUICAO PAGAMENTO LDA
#	12222  EDP DISTRIBUI��O  NOVOS RAMAIS ENERGIA
#	12223  EDP
#	12230  EDP
#	---
#	20108  WIZINK BANK, SA
#	20117  IMPIC  pagamento alvar� constru��o civil e outros
#	20130  NOVO BANCO S.A.
#	20145  SPORTING CLUBE PORTUGAL  FUTEBOL SAD
#	20152  Sporting Clube de Portugal
#	20160  Jogos Santa Casa
#	20173  LIBERTY SEGUROS SA
#	20174  EDP
#	20175  Allianz (Seguros)
#	20181  INSTITUTO GESTAO FINANC SEG SOCIAL
#	20183  Generali (Seguros)
#	20185  BNP PARIBAS PERSONAL FINANCE
#	20204  Adb Aguas de Barcelos S A
#	20223  NOVO BANCO S.A.
#	20229  GE CONSUMER FINANCE IFIC SA.
#	20237  Entidades P�blicas / Execu��es Fiscais / ORDEM DOS SOLICITADORES E AGENTES DE EXECU��O
#	20341  VIA VERDE PORTUGAL  S.G.E.COBRANCAS SA
#	20389  Uzo
#	20394  BANCO COMERCIAL PORTUGUES
#	20409  Federa��o Portuguesa de Futebol
#	20414  BANCO ELECTRONICO SERVICO TOTAL
#	20420  Metlife Europe Limited
#	20426  FCPorto  Porto Comercial SA
#	20442  NOS  ZON Pagamento facturas
#	20484  Caixa Geral de Dep�sitos (ex. carregamento de cart�es de d�bito pr� pagos)
#	20498  BANCO SANTANDER CONSUMER PORTUGAL, SA
#	20592  Optimus Home
#	20601  BNP PARIBAS PERSONAL FINANCE
#	20603  Optimus / Clix
#	20638  Optimos Kanguru  NOS Comunica��es
#	20641  Servi�os Municipalizados de Loures  �guas (eventualmente utilizado tamb�m por outros mun�cipios)
#	20659  Zurich Seguros
#	20669  Munic�pio Oliveira de Azem�is
#	20670  BANCO SANTANDER TOTTA S.A.
#	20678  ONEY / Jumbo
#	20691  SERV. MUNICIPA. DE AGUA E SANEAM. SINTRA
#	20698  Ordem dos Arquitetos
#	20715  BANCO BPI
#	20718  BANCO SANTANDER TOTTA S.A.
#	20719  ASSOCIACAO DNS PT
#	20724  AUTORIDADE PARA CONDICOES TRABALHO
#	20741  CREDIBOM-SOC.FIN.AQUISICAO A CREDITO, SA
#	20754  Santander Totta  Cart�o de cr�dito
#	20755  BANCO SANTANDER TOTTA S.A.
#	20776  AGEAS PORTUGAL COMPANHIA SEGUROS SA
#	20804  UNICRE-INSTITUICAO FINANCEIRA CREDITO SA
#	20811  �guas de Lisboa (EPAL)
#	20812  EDP servi�o universal
#	20813  Banco BPI
#	20815  �guas de Gaia
#	20821  IST, Instituto Superior T�cnico
#	20832  EMPRESA ELECTRICIDADE MADEIRA SA
#	20834  NOVO BANCO S.A.
#	20838  INSTITUTO SUPERIOR ECONOMIA GESTAO
#	20839  Cetelem
#	20843  Pagamento multa / coima rodovi�ria
#	20856  GASCAN, S.A.
#	20858  COFIDIS
#	20890  WIZINK BANK, SA (BARCLAYCARD)
#	20891  Wizink Bank SA  Barclays Cart�o de cr�dito
#	20912  ISPA INST SUPERIOR PSICOLOGIA APLICADA
#	20918  UNIVERSIDADE AVEIRO
#	20931  Rede 4
#	20932  ORDEM DOS CONTABILISTAS CERTIFICADOS
#	20934  A�oreana Seguros
#	20936  NOWO COMMUNICATIONS, SA
#	20950  Petr�leos Portugal Petrogal, SA
#	20961  Rentokill
#	20973  BNP PARIBAS PERSONAL FINANCE
#	20975  Instituto da Mobilidade e dos Transportes, I.P. (IMTT)
#	20977  Remax  Casax, Consultadoria de Gest�o Lda
#	20987  BLUETICKET SERVICOS BILHETICA SA
#	---
#	21000  JET COOLER AGUAS CAFES SA
#	21029  APBP  Artistas Pintores com a Boca e o P�, Lda.
#	21034  BANCO PRIMUS SA
#	21036  MEO
#	21053  PORTO EDITORA, S.A
#	21054  DGEG  Dire��o-Geral de Energia e Geologia
#	21056  Seguran�a Social
#	21058  Vodafone Direto
#	21068  AudioGest  Ass. para a Gest�o e Distribui��o de Direitos
#	21086  INSTITUTO M T TERRESTRES,IP
#	21096  Galp Energia
#	21098  EasyPay (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares. (*)
#	21102  Montepio Cr�dito
#	21111  INSTITUTO GESTAO FINANC SEG SOCIAL
#	21132  �guas do Ribatejo
#	21135  SEGURADORAS UNIDAS SA
#	21142  CONDOARADE-GEST. CONDOMINIOS LDA
#	21146  SEGURIHIGIENE, Sa�de no Trabalho SA
#	21154  CTT (Pagamento Portagens)
#	21159  MEO Pagamento facturas
#	21177  G�s (Galp)
#	21184  COFRE PREVIDENCIA FUNCIONARIOS AGENTES
#	21188  EDP SOLUCOES COMERCIAIS
#	21196  EDP SOLUCOES COMERCIAIS
#	21199  ASSOC.PORT.EMPRESAS CONTAB.ADMINISTRACAO
#	21212  MUNICIPIO PAREDES
#	21217  ASCENDI NORTE AUTO-ESTRADAS DO NORTE SA
#	21218  Ascendi Portagens
#	21225  MONTELLANO LDA
#	21234  Vialivre (Portagens)
#	21235  OTIS ELEVADORES LDA
#	21245  BMW GMBH SUCURSAL PORTUGUESA
#	21246  BMW RENTING PORTUGAL LDA
#	21262  Intrum Justitia
#	21269  UNIVERSIDADE DO PORTO
#	21276  TOTTA SEGUROS-COMP.SEG.DE VIDA,SA
#	21286  MONTEPIO RECUPERACAO DE CREDITO, ACE�
#	21297  GROUPAMA SEGUROS SA
#	21309  MUNICIPIO DE TERRAS DE BOURO
#	21312  CAIXA ECONOMICA MONTEPIO GERAL
#	21318  MUNICIPIO DE COIMBRA
#	21321  PRIMAVERA SOFTWARE, SA
#	21323  321 CREDITO INST FINANCEIRA D CREDITO SA
#	21325  C�mara Municipal de Gaia
#	21341  PORTVIAS  Portagem de Vias, S.A.
#	21344  MUNICIPIO DE GONDOMAR
#	21345  CASCAIS PROXIMA EM SA
#	21347  Pol�cia Municipal de Lisboa
#	21349  SERVDEBT CAPITAL ASSET MANAGEMENT LDA
#	21353  VIALIVRE, SA
#	21365  SERVDEBT CAPITAL ASSET MANAGEMENT LDA
#	21374  BNP PARIBAS PERSONAL FINANCE
#	21375  BANCO COMERCIAL PORTUGUES
#	21383  WURTH PORTUGAL TECNICA DE MONTAGEM, LDA.
#	21410  SERVDEBT CAPITAL ASSET MANAGEMENT LDA
#	21417  ASCENDI PINHAL INTERIOR ESTRADAS PINHAL
#	21423  HPME SA  HI-MEDIA PORTE MONNAIE �LECTRONIQUE (HPME) SA  Entidade que faculta servi�os de pagamento a terceiros
#	21426  PT PAY SA (Servi�os Meo Wallet, TicketLine, outros#)
#	21448  FCT, Fundos de Compensa��o do Trabalho
#	21449  Mun�cipio de Lisboa
#	21467  LIBERTY SEGUROS SA
#	21486  PORTVIAS  Portagem de Vias, S.A.
#	21487- AV-AGUAS VALONGO SA
#	21489  BANCO COMERCIAL PORTUGUES
#	21495  Servi�os Partilhados Minist�rio da Sa�de (SPMS)
#	21496  CMPEA-EMPRESA AGUAS MUNICIPIO PORTO,E.M.
#	21516  EXERCITO PORTUGUES
#	21523  Gestifatura  Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares.
#	21524  �guas do Norte, SA
#	21535  LISGARANTE-SOC.DE GARANTIA MUTUA, SA
#	21540  AEGON SANTANDER PORTUGAL VIDA
#	21546  UNION DE CREDITOS IMOBILIARIOS, SA, EFC
#	21557  CTT  Correios de Portugal (Cobran�a de Servi�os, por ex, �gua da CM Moita, Agere  Braga)
#	21563  PT PAY SA
#	21565  PT PAY SA
#	21572  VITORIA SEGUROS, SA
#	21575  SERVICOS MUNICIPALIZADOS CALDAS RAINHA
#	21577  LEASE PLAN PORTUGAL LDA
#	21579  NOS COMUNICACOES SA
#	21604  EUPAGO INSTITUICAO PAGAMENTO LDA
#	21606  ORDEM DOS ENFERMEIROS
#	21607  CTT EXPRESSO-SERVICO POSTAIS LOGISTICA
#	21615  LOGICOMER GESTAO E RECUP DE CREDITO SA
#	21619  SERVICOS MUNICIPALIZADOS DE LEIRIA
#	21622  �guas de Coimbra
#	21625  SERV. MUNIC. ELECT. AGUAS SANEAM. C. M. MAIA
#	21639  P�ginas Amarelas
#	21643  HEFESTO STC, S.A.
#	21651  �guas de Gaia
#	21653  SAGASTA SA
#	21654  C�mara Municipal do Seixal
#	21662  IFTHENPAY LDA (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	21682  MUNICIPIO DE OEIRAS
#	21721  IFTHENPAY LDA (Servi�o de atribui��o de referencias pagamento MB a pequenas empresas / particulares)
#	21726  GALP POWER, SA
#	21738  SMAS Peniche
#	21800  MEDIAMEDICS BV (*), please check connection with EDP!
#	---
#	---
#	23000  ENTERTAINMENT TECHNOLOGIES LIMITED
#	23002  Circuland SA
#	23013  EDP
#	---
#	24564  �guas da Figueira SA
#
# (*) - care to be taken when using this entity.


# This is a module
if __name__ == "__main__":
    print("import payments.ptpays as ptpays !")
