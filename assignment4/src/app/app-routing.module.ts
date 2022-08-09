import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { HomeComponent } from "./home/home.component";
import { LoginComponent } from "./login/login.component";
import { RegisterComponent } from "./register/register.component";

const appRoute:Routes=[
    {path:'login',component:LoginComponent},
    {path:'register',component:RegisterComponent},
    {path:'dashboard',component:DashboardComponent},
    {path:'',component:HomeComponent,pathMatch:'full'},

];

@NgModule({
    imports:[RouterModule.forRoot(appRoute)],
    exports:[RouterModule]
})

export class AppRoutingModule{

}