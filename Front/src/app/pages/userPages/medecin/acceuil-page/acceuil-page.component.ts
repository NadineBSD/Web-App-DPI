import { Component, inject, OnInit, signal } from '@angular/core';
import { HeaderComponent } from "../../../../components/header-user/header.component";
import { DashBoardComponent } from "../../../../components/dash-board/dash-board.component";
import { LoadingScreenComponent } from "../../../../components/loading-screen/loading-screen.component";
import { UserDataService } from '../../../../services/userData/user-data.service';
import { FetchModulesService } from '../../../../services/fetchModules/fetch-modules.service';
import { Patient } from '../../../../modules/types';
import { DPI } from '../../../../modules/types';
import { catchError } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ZXingScannerModule } from '@zxing/ngx-scanner';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-acceuil-page',
  standalone: true,
  imports: [HeaderComponent, DashBoardComponent, LoadingScreenComponent, CommonModule, FormsModule, ZXingScannerModule],
  templateUrl: './acceuil-page.component.html',
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  styleUrl: './acceuil-page.component.css'
})

export class AcceuilPageComponent implements OnInit {

  isDashBoardVisible = true;
  id!:number;

  isScanning = false;
  onScanSuccess(result: string) {
    console.log('QR Code scanned: ', result);
  }
  onScanFailure(error: any) {
    console.error('Scan failed: ', error);
  }

  user = inject(UserDataService).getUserData() ;  //Njibou Data te3 user te3na 

  isCreeDPI = signal(false);
  isRecherchePatient = signal(false); //si on clique 3la recherche wella créer, ywellou vrai

  updateDashboardVisibility(isVisible: boolean) {
    console.log('Dashboard visibility updated:', isVisible);
    this.isDashBoardVisible = isVisible;
  }

  annulerRecherche(event: MouseEvent){

    if ((event.target as HTMLElement).classList.contains('grey-div') || (event.target as HTMLElement).classList.contains('annuler') ) {
      this.isCreeDPI.set(false);
      this.isRecherchePatient.set(false);
    }
    
  }

  creerDPI(){
    console.log("Créer DPI en cours de traitement...")
  }
  
  
  fetchServices = inject(FetchModulesService);
  listePatient = signal<Array<Patient>>([]);
  listeDPI = signal<Array<DPI>>([]);

  ngOnInit(): void { //when this page load, we fetch the list of patients
      
    this.fetchServices.fetchListePatient().pipe( //pipe to catch any error
      catchError((err) => {
        console.log(err);
        throw err;
      })
      ).subscribe((liste) => {
      this.listePatient.set(liste);
    });

    this.fetchServices.fetchListeDPIs().pipe( //pipe to catch any error
      catchError((err) => {
        console.log(err);
        throw err;
      })
      ).subscribe((liste) => {
        this.listeDPI.set(liste);
        this.transformData()
    })

    const rout = inject(ActivatedRoute);
    rout.paramMap.subscribe((params) =>{
      this.id = Number(params.get("id")); //id de patient récupéré
    });

    
  }

  transformData(){ //id of DPI from string -> int
    this.listeDPI.update((liste) => {
      liste.forEach((d) => d.id = Number(d.id));
      return liste;
    })
  }

  searchedDPI = signal<DPI | null>(null);
  nssInput = '';

  recherchePatient(){

    console.log("Recherche patient en cours de traitement...");
  
  }


}
