 
  // <!-- ======== OWL CAROSUEL ========= -->

        jQuery(document).ready(function ($) {

          // ======== BEST-SELLER ===========
          $(".owl-carousel").owlCarousel({
            loop: true,
            margin: 15,
            autoplay: true,
            autoplayTimeout: 5000,
            nav: true,
            responsiveClass: true,
            responsive: {
              0: {
                items: 1,
                nav: false,
              },
              577: {
                items: 2,
                nav: false,
              },
              780: {
                items: 2,
                nav: true,
              },
              992: {
                items: 3,
                nav: true,
              },
              1184: {
                items: 4,
                nav: true,
              },
            },
          });
        });

  
 	// ======= MOBILE CATEGORY SLIDER  ===============    


		
	 jQuery(document).ready(function($){	
		jQuery('.example-1').square1({caption: 'none',
		theme: 'light'});
  		jQuery('.example-2').square1({animation: 'slide'});
	 });


	// ============ ALL-PRODUCTS ACCORDION =================



  
  