// 
// This controller displays a discharge summary in a large modal.
// 
controllers.controller(
    'ModalDischargeSummaryCtrl',
    function($scope, $modalInstance){

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
            $modalInstance.close('cancel');
        };
        
    }
)
