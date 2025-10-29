класс  Транспорт :
    def  __init__ ( self , id , current_location ):
        self.id = id​ ​ 
        self.current_speed = 0​​  
        self.текущее_местоположение = текущее_местоположение ​​ 
        self.battery_level = 100 ​​ 

    def  move ( self , new_location , speed ):
        требуемый_заряд  =  скорость
        если  self.battery_level < required_charge :​​  
            print ( "Недостаточно заряда для поездки." )
            возвращаться
        self.текущее_местоположение = новое_местоположение​​  
        self.current_speed = скорость​​  
        self.battery_level = max ( self.battery_level - speed , 0 )​​ ​​   

    def  charge ( сам , сумма ):
        self.battery_level = min ( self.battery_level + amount , 100 )​​ ​​   

    def  get_info ( self ):
        return  f"Транспорт { self . id } : скорость { self . current_speed } , место { self . current_location } , заряд { self . Battery_level } %"

класс  ElectricScooter ( транспорт ):
    def  __init__ ( self , id , current_location ):
        super (). __init__ ( id , current_location )
        self.is_rented = Ложь​​  

    def  move ( self , new_location , speed ):
        если  не  self . is_rented :
            print ( "Самокат не арендован." )
            возвращаться
        супер (). перемещение ( новое_местоположение , скорость )

    def  get_info ( self ):
        состояние  =  "арендован",  если  сам . is_rented  еще  "не арендован"
        return  f"Самокат { self . id } : { состояние } , скорость { self . current_speed } , место { self . current_location } , заряд { self . Battery_level } %"

класс  Дрон ( транспорт ):
    def  __init__ ( self , id , current_location ):
        super (). __init__ ( id , current_location )
        собственная высота  =  0​

    def  take_off ( self , value ):
        высота + = значение​  

    def  land ( self ):
        собственная высота  =  0​

    def  move ( self , new_location , speed ):
        если  собственная высота < =  0 : 
            print ( "Дрон не взлетел." )
            возвращаться
        супер (). перемещение ( новое_местоположение , скорость )
        print ( f"Дрон летит в { new_location } на высоте { собственная высота } м ." )

    def  get_info ( self ):
        return  f " Дрон { self.id } : скорость { self.current_speed } , место { self.current_location } , заряд { self.battery_level } % , высота { self.высота } м "​​


класс  GPSNavigator :
    def  calculate_route ( self , from_location , to_location ):
        return  f"Проложен маршрут из { from_location } в { to_location } ."

класс  EmergencyLanding :
    def  perform_emergency_landing ( self ):
        собственная высота  =  0​
        self.current_speed = 0​​  
        self.battery_level = 5​​  
        распечатать ( "Аварийная посадка!" )

класс  DeliveryDrone ( дрон , GPS-навигатор , аварийная посадка ):
    def  __init__ ( self , id , current_location ):
        super (). __init__ ( id , current_location )
        сам . пакет  =  Нет

    def  load_package ( self , package_name ):
        self.package = package_name ​​ 

    def  deliver_package ( self ):
        если  self . altitude  ==  0  и  self . package :
            print ( f"Посылка { self . package } доставлена!" )
            сам . пакет  =  Нет
        еще :
            print ( "Дрон не на земле, невозможно доставить посылку." )

    def  get_info ( self ):
        package_info  =  self . package  if  self . package  else  "нет посылки"
        return  f"Дрон доставки { self.id } : скорость { self . current_speed } , место { self . current_location } , заряд { self . Battery_level } %, высота { self . height } м , посылка: { package_info } "


если  __name__  ==  "__main__" :
    # Транспорт
    t1  =  Транспорт ( «Т-001» , «Склад» )
    печать ( t1 . get_info ())
    т1 . ход ( "Пункт А" , 20 )
    печать ( t1 . get_info ())
    t1 . заряд ( 10 )
    печать ( t1 . get_info ())

    # Электросамокат
    самокат  =  ElectricScooter ( "ES-001" , "Парк" )
    печать ( скутер . get_info ())
    скутер . переезд ( "Магазин" , 15 )
    скутер . is_rented  =  True
    скутер . переезд ( "Магазин" , 15 )
    печать ( скутер . get_info ())
    скутер . зарядка ( 20 )
    печать ( скутер . get_info ())

    # Дрон
    d1  =  Дрон ( «Д-001» , «Гараж» )
    печать ( d1 . get_info ())
    д1 . переезд ( "Город" , 10 )
    d1 . взлет ( 50 )
    д1 . переезд ( "Город" , 10 )
    печать ( d1 . get_info ())
    d1 . земля ()
    печать ( d1 . get_info ())

    # ДоставкаДроном
    dd  =  DeliveryDrone ( «DD-001» , «Склад» )
    печать ( дд . get_info ())
    маршрут  =  дд . вычисление_маршрута ( дд . текущее_локация , "Дом клиента" )
    печать ( маршрут )
    дд . взлет ( 100 )
    дд . load_package ( "Книга" )
    печать ( дд . get_info ())
    дд . переехать ( "Дом клиент" , 30 )
    дд . deliver_package ()
    дд . земля ()
    дд . deliver_package ()
    печать ( дд . get_info ())

    дд . выполнить_аварийную_посадку ()
    печать ( дд . get_info ())