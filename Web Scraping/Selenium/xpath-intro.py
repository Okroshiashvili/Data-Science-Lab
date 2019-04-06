''''




axis::nodetest[predicate]

Of the three components that a location step may contain, only the node test is required. If you omit the axis, you
omit the double colon (::) that delimits it from the node test. If you omit the predicate, you also omit the square
brackets ([ and ]) that enclose it.

The axis selects the direction you're looking; the node test selects particular generic kinds of objects to see; and the
predicate highlights only those objects of the right generic kinds that have other specific characteristics.



pantry/shelf/supplies/paper_goods/paper_good


pantry//paper_good




<pantry>
   <shelf>
      <supplies>
         <paper_goods>
            <paper_good>paper towels</paper_good>
            <paper_good>paper plates</paper_good>
         </paper_goods>
      </supplies>
      <snack_foods>
         <snack_food>popcorn</snack_food>
         <snack_food>chips</snack_food>
      </snack_foods>
   </shelf>
   <shelf>
      <supplies>
         <paper_goods>
            <paper_good>napkins</paper_good>
         </paper_goods>
      </supplies>
      <snack_foods>
         <snack_food>dried tofu</snack_food>
      </snack_foods>
   </shelf>
</pantry>





person/child[@name='Mike']



<person name="John">
   <child name="John"/>
   <child name="Connie"/>
   <child name="Cindy"/>
   <child name="Mike"/>
</person>



'''