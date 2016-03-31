
describe('ModalDischargeSummaryCtrl', function (){
    var $controller, $scope, $modalInstance, $httpBackend, $rootScope, $modal;
    var Episode;
    var episode

    beforeEach(module('opal.controllers'));

    beforeEach(inject(function($injector){
        $rootScope   = $injector.get('$rootScope');
        $scope       = $rootScope.$new();
        $modal       = $injector.get('$modal');
        $controller  = $injector.get('$controller');
        $httpBackend = $injector.get('$httpBackend');
        Episode      = $injector.get('Episode');

        $modalInstance = $modal.open({template: 'Not a real template'});
        episode = new Episode({demographics: [{patient_id: 1}]});
        controller = $controller('ModalDischargeSummaryCtrl', {
            $scope        : $scope,
            $modalInstance: $modalInstance,
            episode       : episode
        });

    }));


    describe('cancel()', function (){
        it('Should close the modal', function () {
            spyOn($modalInstance, 'close');
            $scope.cancel();
            expect($modalInstance.close).toHaveBeenCalledWith('cancel');
        });
    });

});
