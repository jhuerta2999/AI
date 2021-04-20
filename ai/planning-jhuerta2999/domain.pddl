(define (domain sokorobotto)
  (:requirements :strips :typing)
    (:types saleitem robot pallette location shipment order - object
              robot pallette - occupies
              order shipment - package
    )  
  (:predicates  
      (orders ?a - order ?b - saleitem) ;a order contains b
      (includes ?a - package ?b - saleitem);simpment (?a) includes ?b
      (connected ?a ?b - location);a connected to b
      (no-Robot ?a - location) ; no robot at ?a
      (free ?a - robot);a not carrying pallette
      (no-pallette ?a - location);no pallette at a
      (ships ?a - shipment ?b - order);a ships to b
      (unstarted ?a - shipment);unstarted T/F
      (packing-location ?a - location) ;a is packing location
      (available ?a - location);packing loc(a) available
      (contains ?a - pallette ?b - saleitem);a contains b
      (at ?a - occupies ?b - location);pallette/robot(a) at b
    ) 

  (:action moveRobot
      :parameters (?from ?to - location ?robot - robot)  
      ;No robot at new location - Locations are connected - Robot at old lcoation
      :precondition (and (no-robot ?to) (at ?robot ?from) 
                      (connected ?from ?to) (connected ?to ?from)
      )         
      ;Robot at new location - No robot at old location
      :effect (and (at ?robot ?to) (not(no-robot ?to)) 
                  (not(at ?robot ?from)) (no-robot ?from) 
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
    )
  )  

  (:action bringValidPallette
      :parameters (?from ?to - location  ?robot - robot ?pallette - pallette  ?item - saleitem ?order - order)
      ;Pallette contains item - Packing location is available - No robot/pallette at new location - Locations are connected - Robot/Pallete at location
      :precondition (and (at ?robot ?from) (at ?pallette ?from)
                      (connected ?from ?to) (connected ?to ?from)
                      (contains ?pallette ?item)
                      (no-robot ?to) (no-pallette ?to) 
                      (orders ?order ?item)
      )
      ;No robot/pallette at old location - Robot/Pallette at new location
      :effect (and (no-robot ?from) (no-pallette ?from)
                  (not(at ?robot ?from)) (not(at ?pallette ?from))
                  (at ?robot ?to) (at ?pallette ?to) 
                  (not (no-pallette ?to)) (not (no-robot ?to))
      )
  )

  (:action unloadPallette
    :parameters (?pallette - pallette ?item - saleitem ?order - order ?ships - shipment ?packing ?to - location ?robot - robot)
    ;Pallette at packing - Pallette contains item - Order unstarted - Order requires item - Packing available - Shipments ships order
    :precondition (and (at ?pallette ?packing) (contains ?pallette ?item)
                      (at ?robot ?packing)
                      (unstarted ?ships) (orders ?order ?item)
                      (ships ?ships ?order) (available ?packing) 
                      (no-robot ?to) (no-pallette ?to)
                      (connected ?packing ?to) (connected ?to ?packing)
    )
    ;Pallette no longer contains item - Order started - Item no longer required - Packing not available
    :effect (and (not (contains ?pallette ?item)) (not (orders ?order ?item))  
                (includes ?order ?item) (includes ?ships ?item)
                (not (no-robot ?to)) (not (no-pallette ?to))
                (at ?robot ?to) (at ?pallette ?to)
                (not (at ?robot ?packing)) (not (at ?pallette ?packing))
                (no-pallette ?packing) (no-robot ?packing)
    )
  )
)