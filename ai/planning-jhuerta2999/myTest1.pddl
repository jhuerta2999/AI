(define (problem soko-ichii-pallette)
  (:domain sokorobotto)
  (:objects
    shipment1 shipment2 - shipment
    order1 order2 - order
    loc1 loc2 loc3 pack1 - location
    robot1 - robot
    pallette1 pallette2 - pallette
    socks1 book1 socks2 book2 - saleitem
    )
  (:init
    (ships shipment1 order1)
    (orders order1 book1)
    (unstarted shipment1)
    
    (ships shipment2 order2)
    (orders order2 socks2)
    (orders order2 book1)
    (unstarted shipment2)
    
    (packing-location pack1)
    (available pack1)
    
    (contains pallette1 book2)
    (contains pallette2 book1)
    
    (free robot1)
    (connected loc1 loc2)
    (connected loc2 loc1)
    (connected loc2 pack1)
    (connected pack1 loc2)
    
    (at pallette2 loc1)
    (at pallette1 loc2)
    (at robot1 loc2)
    (no-robot loc1)
    (no-robot pack1)
    (no-pallette pack1)

    )
  (:goal (and (includes shipment1 socks1)
              ))
)
