(define (domain smallSokorobotto)
    (:requirements :strips :typing :action-costs :negative-preconditions)
      (:types saleitem robot pallette location shipment order - object
                robot pallette - occupies
                order shipment - package
                )  
    (:predicates  
        (orders ?a - order ?b - saleitem) ;a order contains b
        (includes ?a - package ?b - saleitem);simpment (?a) includes ?b
        (connected ?a ?b - location);a connected to b
        (robot ?a - robot);robot ?a;
        (no-Robot ?a - location) ; no robot at ?a
        (free ?a - robot);a not carrying pallette
        (pallette ?a - pallette);a pallette
        (no-pallette ?a - location);no pallette at a
        (sale-items ?a - saleitem);a is a sale item
        (ships ?a - shipment ?b - order);a ships to b
        (unstarted ?a - shipment);unstarted T/F
        (packing-location ?a - location) ;a is packing location
        (available ?a - location);packing loc(a) available
        (contains ?a - pallette ?b - saleitem);a contains b
        (at ?a - occupies ?b - location);pallette/robot(a) at b
      ) 
    ;GOOD
    (:action moveRobot
        :parameters (?from - location ?to - location ?robot - robot)  
        ;No robot at new location - Locations are connected - Robot at old lcoation
        :precondition (and (no-robot ?to) (at ?robot ?from) 
                        (connected ?from ?to) (connected ?to ?from)
        )         
        ;Robot at new location - No robot at old location
        :effect (and (at ?robot ?to) (no-robot ?from) 
                    (not(at ?robot ?from)) (not(no-robot ?to))
        ) 
    )
    ;GOOD
    (:action carryPallette
        :parameters (?robot - robot ?pallette - pallette ?item - saleitem ?location - location)
        ;Robot is free - Robot at location - Pallette at location
        :precondition (and (free ?robot) (at ?robot ?location) (at ?pallette ?location)
        )
        :effect (and (not (free ?robot))
        )
    )

    (:action bringValidPallette
        :parameters (?location ?from ?to ?packing - location  ?robot - robot ?pallette - pallette  ?item - saleitem ?order - order)
        ;Pallette contains item - Packing location is available - No robot/pallette at new location - Locations are connected - Robot/Pallete at location
        :precondition (and (at ?robot ?from) (at ?pallette ?from)
                        (connected ?from ?packing) (connected ?packing ?from)
                        (contains ?pallette ?item) (available ?packing)
                        (no-robot ?to) (no-pallette ?to) 
                        (orders ?order ?item)
        )
        ;No robot/pallette at old location - Robot/Pallette at new location
        :effect (and (no-robot ?from) (no-pallette ?from)
                (at ?robot ?to) (at ?pallette ?to) 
                (not (no-pallette ?to)) (not (no-robot ?to))
                (not(at ?robot ?from)) (not(no-robot ?from))
                (not(at ?pallette ?from)) (not(no-pallette ?from))
        )
    )

    (:action movePallette
      :parameters (?pallette - pallette ?robot - robot ?from ?to - location)
      ;New location no robot - New Location no pallete - locations connected - Robot/Pallette at old location 
      :precondition (and (at ?pallette ?from) (at ?robot ?from)
                        (no-pallette ?to) (no-robot ?to)
                        (connected ?from ?to) (connected ?to ?from)
      )
      ;Robot/Pallette at new location - No robot/pallette at old location
      :effect (and (at ?robot ?to) (at ?pallette ?to)
                    (no-pallette ?from) (no-robot ?from)
                    (not (no-pallette ?to)) (not (no-robot ?to))
                    (not(at ?robot ?from)) (not(at ?pallette ?from))
                    (not(no-pallette ?from)) (not(no-robot ?from))
      )
    )  
    ;UNLOAD ITEM FROM ONE PALLETTE
    (:action unloadPallette
      :parameters (?pallette - pallette ?item - saleitem ?order - order ?ships - shipment ?packing ?location - location)
      ;Pallette at packing - Pallette contains item - Order unstarted - Order requires item - Packing available - Shipments ships order
      :precondition (and (at ?pallette ?packing) (contains ?pallette ?item)
                        (unstarted ?ships) (orders ?order ?item)
                        (ships ?ships ?order) (available ?packing) 
      )
      ;Pallette no longer contains item - Order started - Item no longer required - Packing not available
      :effect (and (not (contains ?pallette ?item)) (not (unstarted ?ships)) 
                    (not (orders ?order ?item)) (not (available ?packing))  
                    (includes ?order ?item) (includes ?ships ?item)
      )
    )
    ;ALLOWS TO UNLOAD MULTIPLE ITEMS FROM 1 PALLETTE
    (:action continueUnloading
        :parameters (?pallette - pallette ?item - saleitem ?order - order ?ships - shipment ?packing ?location - location)
        :precondition (and (at ?pallette ?packing) (contains ?pallette ?item) (not (unstarted ?ships)) 
                            (orders ?order ?item) (ships ?ships ?order) (not (available ?packing)))
        :effect (and (not (contains ?pallette ?item)) (not (orders ?order ?item))
                    (includes ?order ?item) (includes ?ships ?item)
        )
    )
      
    (:action removePallette
      :parameters (?pallette - pallette ?robot - robot ?packing ?to - location ?shipment - shipment)
      ;Robot/Pallette at Packing - No robot/pallette at new loc - New loc next to Packing - Shipment started - Packing not available 
      :precondition (and  (at ?pallette ?packing) (at ?robot ?packing)
                          (no-pallette ?to) (no-robot ?to)
                          (connected ?packing ?to) (connected ?to ?packing)
                          (not (unstarted ?shipment)) (not (available ?packing))
      )
      ;No robot/pallette at packing - Robot/Pallette at new loc - Shipment unstarted - Packing available
      :effect (and (not(at ?robot ?packing)) (not(at ?pallette ?packing))
                    (at ?robot ?to) (at ?pallette ?to)
                    (unstarted ?shipment) (available ?packing)

      )
    )
    
) 